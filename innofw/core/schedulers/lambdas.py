import torch


def dummy_func(epoch):
    print('here')
    print(1/ 0 )
    return (epoch * 0.01) + 0.05

def func():
    return lambda epoch: epoch // 30
lambda1 = func

# cfg = DictConfig({"_target_": "torch.optim.lr_scheduler.LambdaLR", "lr_lambda": {"_target_": "innofw.core.schedulers.lambdas.lambda1"}})