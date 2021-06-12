# -*- coding: utf-8 -*-
import mySettings
import tensorflow as tf
import numpy as np
from imageio import imread, imsave
import os
import time

def the_current_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))

def transfer(style,content):
    model = 'samples_styles/%s' % style  # 风格模型名称
    content_image = "content/%s" % content  # 内容图片
    result_image = 'transfer_out/%s_%s' % (style, content)  # 迁移后的图片
    X_image = imread(content_image)  # 读取内容图片

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    # 加载训练好的模型
    saver = tf.train.import_meta_graph(os.path.join(model, 'fast_style_transfer.meta'))
    saver.restore(sess, tf.train.latest_checkpoint(model))

    graph = tf.get_default_graph()
    X = graph.get_tensor_by_name('X:0')
    g = graph.get_tensor_by_name('transformer/g:0')

    gen_img = sess.run(g, feed_dict={X: [X_image]})[0]
    gen_img = np.clip(gen_img, 0, 255) / 255.
    imsave(result_image, gen_img)
    # the_current_time()
    return result_image

# if __name__ == '__main__':
#     style = mySettings.style_name  # 风格名称
#     content = mySettings.content_image # 内容名称
#
#     model = 'samples_styles/%s' % style # 风格模型名称
#     content_image = "content/%s"%content # 内容图片
#     result_image = 'transfer_out/%s_%s' % (style,content) # 迁移后的图片
#     X_image = imread(content_image)  # 读取内容图片
#
#     sess = tf.Session()
#     sess.run(tf.global_variables_initializer())
#
#     # 加载训练好的模型
#     saver = tf.train.import_meta_graph(os.path.join(model, 'fast_style_transfer.meta'))
#     saver.restore(sess, tf.train.latest_checkpoint(model))
#
#     graph = tf.get_default_graph()
#     X = graph.get_tensor_by_name('X:0')
#     g = graph.get_tensor_by_name('transformer/g:0')
#
#     the_current_time()
#
#     gen_img = sess.run(g, feed_dict={X: [X_image]})[0]
#     gen_img = np.clip(gen_img, 0, 255) / 255.
#     imsave(result_image, gen_img)
#     the_current_time()
