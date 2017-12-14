
from thumbnail_maker import ThumbnailMakerService

IMG_URLS = [
  # 'https://dl.dropboxusercontent.com/s/2fu69d81fesbhru/pexels-photo-48603.jpeg',
  'https://dl.dropboxusercontent.com/s/zch88m6sb8a7bm1/pexels-photo-48603.jpeg',
]

def test_thumbnail_maker():
  tn_maker = ThumbnailMakerService()
  tn_maker.make_thumbnails(IMG_URLS)
