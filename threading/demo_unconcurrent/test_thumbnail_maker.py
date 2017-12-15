
from thumbnail_maker import ThumbnailMakerService

IMG_URLS = [
  'https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg',
  'https://dl.dropboxusercontent.com/s/zch88m6sb8a7bm1/pexels-photo-134392.jpeg',
  'https://dl.dropboxusercontent.com/s/lsr6dxw5m2ep5qt/pexels-photo-135130.jpeg',
  'https://dl.dropboxusercontent.com/s/6xinfm0lcnbirb9/pexels-photo-167300.jpeg',
  'https://dl.dropboxusercontent.com/s/2dp2hli32h9p0y6/pexels-photo-167921.jpeg',
  'https://dl.dropboxusercontent.com/s/fjb1m3grcrceqo2/pexels-photo-173125.jpeg',
  'https://dl.dropboxusercontent.com/s/56u8p4oplagc4bp/pexels-photo-185934.jpeg',
  'https://dl.dropboxusercontent.com/s/2s1x7wz4sdvxssr/pexels-photo-192454.jpeg',
  'https://dl.dropboxusercontent.com/s/1gjphqnllzm10hh/pexels-photo-193038.jpeg',
  'https://dl.dropboxusercontent.com/s/pcjz40c8pxpy057/pexels-photo-193043.jpeg',
]

def test_thumbnail_maker():
  tn_maker = ThumbnailMakerService()
  tn_maker.make_thumbnails(IMG_URLS)
