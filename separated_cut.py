import cv2
import numpy as np
import math

# source_image_path='D:/원본데이터/Webtoon_merge_resizing/test_webtoon_001.png'

'''
for file_number in range(11,12):
    
    file_number=str(file_number).zfill(3)
    print('No.',file_number)
    
    # source image 가져오기
    source_image_path='./test_webtoon_{}.png'.format(file_number)
    source_image = cv2.imread(source_image_path)
    print('source_image type : ',type(source_image))
    print("source_image height = ", source_image.shape[0])

    # source image 가로/세로 길이 구하기
    # shape() => (height, width, channel)
    source_image_height=source_image.shape[0]
    source_image_width=source_image.shape[1]
    
    before_ceil=source_image_height/2
    divde_source_image_height=math.ceil(source_image_height//2) # 소수점 버리고 정수 부분만 남김
    print('source_image_width = {}'.format(source_image_width))
    print('before_ceil = {}'.format(before_ceil))
    print('source_image_height = {} \t divde_source_image_height = {}'.format(source_image_height,divde_source_image_height))
   
    print('cut_image_1 height range : 0 ~ ',divde_source_image_height-1)
    print('cut_image_2 height range : {} ~ {}'.format(divde_source_image_height,source_image_height))
    
    # 분할 컷
    cut_image_1=source_image[:divde_source_image_height]
    cut_image_2=source_image[divde_source_image_height:]
      
    # # source image와 cut image 두 장 확인
    # cv2.imshow("source_image", source_image)
    # cv2.imshow("cut_image_1", cut_image_1)
    # cv2.imshow("cut_image_2", cut_image_2)

    # cut image 저장
    cv2.imwrite('./9_Image_split/test_webtoon_{}_1_9.png'.format(file_number),cut_image_1)
    cv2.imwrite('./9_Image_split/test_webtoon_{}_2_9.png'.format(file_number),cut_image_2)
    
    print()
    '''

convert_to_jpeg__failed_list=[5,13,14,18,21,23,26,31,32,33,38,47,59,62,72,76,77,89,91,93,96,99,125,129,131,138,143,145,149,150]
print('convert_to_jpeg__failed_list length : ',len(convert_to_jpeg__failed_list))
    
    
for file_number in range(6,151):
    
    file_number=str(file_number).zfill(3)
    print('No.',file_number)
    
    # 합칠 이미지 3개 가져오기
    source_image_path1='./9_Image_split/test_webtoon_{}_1_9.png'.format(file_number)
    source_image_path2='./9_Image_split/test_webtoon_{}_2_9.png'.format(file_number)
    space_image_path='./9_Image_split/space_area.png'
    source_image1 = cv2.imread(source_image_path1)
    source_image2 = cv2.imread(source_image_path2)
    space_image = cv2.imread(space_image_path)


    # source image, space image 가로/세로 길이 구하기
    # shape() => (height, width, channel)
    source_image1_height=source_image1.shape[0]
    source_image1_width=source_image1.shape[1]
    
    source_image2_height=source_image2.shape[0]
    source_image2_width=source_image2.shape[1]
    
    space_image_height=space_image.shape[0]
    space_image_width=space_image.shape[1]
    
    print("source_image1 height = ", source_image1_height)
    print("source_image2 height = ", source_image2_height)
    print("space_image height = ", space_image_height)
    
    print("source_image1 width = ", source_image1_width)
    print("source_image2 width = ", source_image2_width)
    
    resize_space_image=space_image[:space_image_height,:source_image1_width]
    print("space_image width = {} -> after resize width = {}".format(space_image_width, resize_space_image.shape[1]))
    print('resize_space_image shape : ',resize_space_image.shape)

    # source_image1, source_image2, resize_space_image 합치기
    merge_image=cv2.vconcat([source_image1,resize_space_image,source_image2])    
    print('merge_image shape : ',merge_image.shape)
    print('merge_image height = {} and merge_image width = {}'.format(merge_image.shape[0],merge_image.shape[1]))


    # merge image 저장
    cv2.imwrite('./Image_split/test_webtoon_{}_9.png'.format(file_number),merge_image)
    
    print()


cv2.waitKey()

