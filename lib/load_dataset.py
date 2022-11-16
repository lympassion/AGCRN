import os
import numpy as np

def load_st_dataset(dataset):
    #output B, N, D
    """
    返回车流量
    :param dataset:
    :return:
    """
    if dataset == 'PEMSD4':
        data_path = os.path.join('../data/PeMSD4/pems04.npz')
        # 数据集的详细说明查看github中，这里shape=(16992, 307, 3)
        # 3 代表三个特性flow, occupy, speed.所以这里仅仅使用了车流量
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    elif dataset == 'PEMSD8':
        data_path = os.path.join('../data/PeMSD8/pems08.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    else:
        raise ValueError

    #
    # print('begin')
    # print(np.load(data_path).files)
    # print(np.load(data_path)['data'])
    #
    # print(type(np.load(data_path)['data']))
    # print(np.load(data_path)['data'].shape)
    # print(np.load(data_path)['data'][:, :, 0].shape)
    # print(len(np.load(data_path)['data'][:, :, 0].shape))
    # print('finished')


    if len(data.shape) == 2:
        data = np.expand_dims(data, axis=-1)
    print('Load %s Dataset shaped: ' % dataset, data.shape, data.max(), data.min(), data.mean(), np.median(data))
    return data
