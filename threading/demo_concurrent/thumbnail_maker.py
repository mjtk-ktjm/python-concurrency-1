import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
import threading

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='testing.log', \
  level=logging.DEBUG, \
  format=FORMAT)

class ThumbnailMakerService(object):
  """Download and resize a list of images."""
  def __init__(self, home_dir='.'):
    self.home_dir = home_dir
    self.input_dir = self.home_dir + os.path.sep + 'incoming'
    self.output_dir = self.home_dir + os.path.sep + 'outgoing'
    self.total_size = 0
    self.lock = threading.Lock()

  def download_image(self, url):
    if not url:
      return

    logging.info("Downloading {}...".format(url))
    img_filename = urlparse(url).path.split('/')[-1]
    img_dest = self.input_dir + os.path.sep + img_filename
    urlretrieve(url, img_dest)
    this_size = os.path.getsize(img_dest)

    self.lock.acquire()
    try:
      self.total_size += this_size
    finally:
      self.lock.release()

    # Preferred method would always actually be with context handler
    # with self.lock:
    #   self.total_size += this_size

    logging.info("Done saving to {}, took {} bytes.".format(img_dest, this_size))

  def download_images(self, img_url_list):
    if not img_url_list:
      return

    os.makedirs(self.input_dir, exist_ok=True)

    logging.info("beginning image downloads...")

    start = time.perf_counter()

    threads = []
    for url in img_url_list:
      t = threading.Thread(target=self.download_image, args=(url,))
      t.start()
      threads.append(t)

    for t in threads:
      t.join()

    end = time.perf_counter()

    logging.info("downloaded {} images ({} bytes) in {} seconds.".format(len(img_url_list), self.total_size, end - start))

  def perform_resizing(self):
    if not os.listdir(self.input_dir):
      return
    os.makedirs(self.output_dir, exist_ok=True)

    logging.info("beginning image resizing...")

    target_sizes = [32, 64, 200]
    num_images = len(os.listdir(self.input_dir))

    start = time.perf_counter()
    for filename in os.listdir(self.input_dir):
      orig_img = Image.open(self.input_dir + os.path.sep + filename)
      for basewidth in target_sizes:
        img = orig_img
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)

        new_filename = os.path.splitext(filename)[0] + \
          '_' + str(basewidth) + os.path.splitext(filename)[1]
        img.save(self.output_dir + os.path.sep + new_filename)

      os.remove(self.input_dir + os.path.sep + filename)

    end = time.perf_counter()

    logging.info("created {} thumbs in {} seconds".format(num_images, end-start))

  def make_thumbnails(self, img_url_list):
    logging.info("Start make_thumbnails")

    start = time.perf_counter()
    self.download_images(img_url_list)
    # self.perform_resizing()
    end = time.perf_counter()

    logging.info("END make_thumbnails in {} seconds".format(end-start))


