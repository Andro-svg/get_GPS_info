import exifread

def read():
  GPS = {}
  date = ''
  f = open("D:\\test_img\\DJI_0569_R.JPG",'rb')
  contents = exifread.process_file(f)
  for key in contents:
    if key == "GPS GPSLongitude":
      # a = contents[key].values
      print("经度 =", contents[key], contents['GPS GPSLongitudeRef'])

    elif key =="GPS GPSLatitude":
      print("纬度 =",contents[key],contents['GPS GPSLatitudeRef'])
    elif key =='GPS GPSAltitudeRef':
      print("高度 =", contents[key], contents['GPS GPSAltitudeRef'])
read()