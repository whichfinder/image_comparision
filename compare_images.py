from PIL import Image
import urllib, requests, cStringIO
url1 = raw_input()
url2 = raw_input()

def compare_two_image(url1, url2):
  transform_url(url1)
  transform_url(url2)
  img1 = Image.open(cStringIO.StringIO(urllib.urlopen(url1).read()))
  img2 = Image.open(cStringIO.StringIO(urllib.urlopen(url2).read()))
  if img1.histogram() == img2.histogram() and img1.getbands() == img2.getbands():
    print 'identical'
  else:
    print set(img1.histogram()) & set(img2.histogram())
    print img1.getbands()
    print img2.getbands()
    print 'different'

def transform_url(url):
  return url.replace('https', 'http')

if __name__ == '__main__':
    compare_two_image(url1, url2)
