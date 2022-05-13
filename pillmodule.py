from PIL import Image
from PIL import ImageFilter

img = Image.open('C:/Users/mong/Desktop/likelion/image.jpg')
print(type(img))

#img.show()

#이미지 크기 변경하기 + 이미지 파일로 저장하기
img_resize = img.resize((300, 300))
img_resize.save('C:/Users/mong/Desktop/likelion/resize.jpg')

#이미지 45도 회전시키기 + 이미지 파일로 저장하기
img_rotate = img.rotate(45)
img_rotate.save('C:/Users/mong/Desktop/likelion/rotate.jpg')

#이미지 필터 사용해서 블러 처리하기 + 이미지 파일로 저장하기
img_blur = img.filter(ImageFilter.BoxBlur(10))
img_blur.save('C:/Users/mong/Desktop/likelion/blur.jpg')

#새로운 컬러 이미지 생성 후, 앞에서 저장한 3개의 이미지를 모두 합치기
new_img = Image.new("RGB", (3000, 3000), 430000)
new_img.paste(img,(10,10))
new_img.paste(img_resize,(img.width + 10, 10))
new_img.paste(img_rotate,(10, img.height +10))
new_img.paste(img_blur,(img.width + 10, img.height +10))

#합친 이미지 바로 보여주기
new_img.show()