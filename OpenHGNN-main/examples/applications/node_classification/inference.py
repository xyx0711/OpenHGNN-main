import argparse
from openhgnn import Experiment
from openhgnn.dataset import AsNodeClassificationDataset
from dataset import MyNCDataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', default='RGCN', type=str, help='name of models')
    parser.add_argument('--dataset', '-d', default='acm', type=str, help='acm or cora')
    parser.add_argument('--gpu', '-g', default='-1', type=int, help='-1 means cpu')
    parser.add_argument('--mini-batch-flag', action='store_true')

    args = parser.parse_args()
    ds = MyNCDataset()
    new_ds = AsNodeClassificationDataset(ds, target_ntype='author', labeled_nodes_split_ratio=[0.8, 0.1, 0.1],
                                         prediction_ratio=1)

    experiment = Experiment(conf_path='../my_config.ini', max_epoch=0, model=args.model, dataset=new_ds,
                            task='node_classification', mini_batch_flag=args.mini_batch_flag, gpu=args.gpu,
                            test_flag=False, prediction_flag=True, batch_size=100, load_from_pretrained=True, use_uva=False)
    prediction_res = experiment.run()
    indices, y_predicts = prediction_res

    print('indices shape', indices.shape)
    print('y_predicts shape', y_predicts.shape)
