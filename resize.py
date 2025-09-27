import os
import cv2
import numpy

from PIL import Image
import os.path as osp


def resize_img(DATADIR, data_k, img_size):
    w = img_size[0]
    h = img_size[1]
    path = os.path.join(DATADIR, data_k)
    # 返回path路径下所有文件的名字，以及文件夹的名字，
    img_list = os.listdir(path)

    for i in img_list:
        if i.endswith('.png'):
            # 调用cv2.imread读入图片，读入格式为IMREAD_COLOR
            img_array = cv2.imread((path + '/' + i), cv2.IMREAD_GRAYSCALE)  # 单通道
            # 调用cv2.resize函数resize图片
            new_array = cv2.resize(img_array, (w, h), interpolation=cv2.INTER_CUBIC)
            img_name = str(i)
            '''生成图片存储的目标路径'''
            save_path = path + '_new1/'

            if os.path.exists(save_path):
                print(i)
                '''调用cv.2的imwrite函数保存图片'''
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)
            else:
                os.mkdir(save_path)
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)


def resize_imgPIL_L(DATADIR, data_k):
    # w = img_size[0]
    # h = img_size[1]
    dir = os.path.join(DATADIR, data_k)
    # 返回path路径下所有文件的名字，以及文件夹的名字，
    files = os.listdir(dir)

    files.sort()
    for each_bmp in files:  # 遍历，进行批量转换
        first_name, second_name = os.path.splitext(each_bmp)
        each_bmp = os.path.join(dir, each_bmp)
        image = Image.open(each_bmp)
        # image = image.convert('RGB')
        # w, h = image.size  # 获取图片的原始尺寸
        # background = Image.new('RGB', size=(max(w, h), max(w, h)))  # 根据原始尺寸 创建较长为边的背景图，颜色值为127
        # len = int(abs(w - h) // 2)  # 一侧需要填充的长度
        # box = (len, 0) if w < h else (0, len)  # 图片粘贴的位置 即图片的位置，从左上开始 假设w=10,h=8,则粘填位置（0，1），从左往右0长度，从上往下1长度，图片粘在背景上
        # background.paste(image, box)
        # image_data = background.resize((256, 256))  # 缩放
        image_data = image.resize((256, 256))  # 缩放
        # image_data  = image_data.convert('L')
        image_data = cv2.cvtColor(numpy.asarray(image_data), cv2.COLOR_RGB2BGR)

        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
        image_data[image_data > 10] = 255

        save_path = dir + '_new1/'
        if os.path.exists(save_path):
            print(first_name)
            '''调用cv.2的imwrite函数保存图片'''
            save_img = save_path + first_name
            save_path = osp.join(save_img + ".png")
            cv2.imwrite(save_path, image_data)
            # image_data.save(save_img + '.png')

        else:
            os.mkdir(save_path)
            save_img = save_path + first_name
            save_path = osp.join(save_img + ".png")
            cv2.imwrite(save_path, image_data)
            # image_data.save(save_img + '.png')


def resize_imgPIL_I(DATADIR, data_k):
    # w = img_size[0]
    # h = img_size[1]
    dir = os.path.join(DATADIR, data_k)
    # 返回path路径下所有文件的名字，以及文件夹的名字，
    files = os.listdir(dir)

    files.sort()
    for each_bmp in files:  # 遍历，进行批量转换
        first_name, second_name = os.path.splitext(each_bmp)
        each_bmp = os.path.join(dir, each_bmp)
        image = Image.open(each_bmp)
        image = image.convert('RGB')
        # w, h = image.size  # 获取图片的原始尺寸
        # background = Image.new('RGB', size=(max(w, h), max(w, h)), color=(255, 255, 255))  # 根据原始尺寸 创建较长为边的背景图，颜色值为127
        # len = int(abs(w - h) // 2)  # 一侧需要填充的长度
        # box = (len, 0) if w < h else (0, len)  # 图片粘贴的位置 即图片的位置，从左上开始 假设w=10,h=8,则粘填位置（0，1），从左往右0长度，从上往下1长度，图片粘在背景上
        # background.paste(image, box)
        # image_data = background.resize((256, 256))  # 缩放
        image_data = image.resize((256, 256))  # 缩放
        image_data = image_data.convert('RGB')
        save_path = dir + '_new1/'
        if os.path.exists(save_path):
            print(first_name)
            '''调用cv.2的imwrite函数保存图片'''
            save_img = save_path + first_name
            image_data.save(save_img + '.png')

        else:
            os.mkdir(save_path)
            save_img = save_path + first_name
            image_data.save(save_img + '.png')


def text1(DATADIR, data_k1, data_k2, base):
    train_image_dir = os.path.join(DATADIR, data_k1)
    train_mask_dir = os.path.join(DATADIR, data_k2)

    imageList = []
    maskList = []
    train_image_fnames = os.listdir(train_image_dir)
    for name in train_image_fnames:
        imageList.append(train_image_dir + '\\' + name)

    train_mask_fnames = os.listdir(train_mask_dir)
    for name in train_mask_fnames:
        maskList.append(train_mask_dir + '\\' + name)

    text_dir = os.path.join(DATADIR, base)

    textfile = open(text_dir, "w")
    for im, mas in zip(imageList, maskList):
        textfile.write(im + ' ' + mas + "\n")
    textfile.close()


def text(DATADIR, data_k1, data_k2, base):
    train_image_dir = os.path.join(DATADIR, data_k1)
    train_mask_dir = os.path.join(DATADIR, data_k2)

    imageList = []
    maskList = []

    train_image_fnames = sorted(os.listdir(train_image_dir))
    train_mask_fnames = sorted(os.listdir(train_mask_dir))

    for img_name, mask_name in zip(train_image_fnames, train_mask_fnames):
        imageList.append(os.path.join(train_image_dir, img_name))
        maskList.append(os.path.join(train_mask_dir, mask_name))

    text_dir = os.path.join(DATADIR, base)

    with open(text_dir, "w") as textfile:
        for im, mas in zip(imageList, maskList):
            textfile.write(im + ' ' + mas + "\n")


def text2(DATADIR, data_k1, data_k2, base):
    train_image_dir = os.path.join(DATADIR, data_k1)
    train_mask_dir = os.path.join(DATADIR, data_k2)

    imageList = [os.path.join(train_image_dir, name) for name in os.listdir(train_image_dir)]
    maskList = [os.path.join(train_mask_dir, name) for name in os.listdir(train_mask_dir)]

    text_dir = os.path.join(DATADIR, base)

    with open(text_dir, "w") as textfile:
        for im_path in imageList:
            im_name = os.path.splitext(os.path.basename(im_path))[0]
            matching_mask = next((mask for mask in maskList if im_name in os.path.splitext(os.path.basename(mask))[0]), None)
            if matching_mask:
                textfile.write(f"{im_path} {matching_mask}\n")


if __name__ == '__main__':
    # 设置图片路径
    DATADIR = r"codes/data_edmcrack600/"
    # DATADIR = "D:\\BaiduNetdiskDownload\\DeepCrack-datasets\\CrackLS315"

    data_k = 'Training_labels'
    data_k1 = 'Training_Images'
    data_k2 = 'val_labels'
    data_k3 = 'val_Images'
    data_k4 = 'Test_labels'
    data_k5 = 'Test_Images'
    # 设置目标像素大小，此处设为128 * 256
    # img_size = [256, 256]
    # resize_img(DATADIR, data_k, img_size)

    resize_imgPIL_L(DATADIR, data_k)
    resize_imgPIL_I(DATADIR, data_k1)
    resize_imgPIL_L(DATADIR, data_k2)
    resize_imgPIL_I(DATADIR, data_k3)
    resize_imgPIL_L(DATADIR, data_k4)
    resize_imgPIL_I(DATADIR, data_k5)

    data_k_new = 'Training_labels_new1'
    data_k1_new1 = 'Training_Images_new1'
    data_k2_new2 = 'val_labels_new1'
    data_k3_new3 = 'val_Images_new1'
    data_k4_new4 = 'Test_labels_new1'
    data_k5_new5 = 'Test_Images_new1'

    base1 = 'train.txt'
    base2 = 'val.txt'
    base3 = 'test.txt'

    text(DATADIR, data_k1_new1, data_k_new, base1)
    text(DATADIR, data_k3_new3, data_k2_new2, base2)
    text(DATADIR, data_k5_new5, data_k4_new4, base3)
