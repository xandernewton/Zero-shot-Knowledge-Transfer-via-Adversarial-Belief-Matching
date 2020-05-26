import No_Teacher
import zero_shot
import KD_AT
import argparse
import utils
import config
import os
import pathlib

if __name__ == "__main__":
    utils.setup_seeds(config.seed)

    os.chdir(pathlib.Path(__file__).parent.absolute())

    mode = config.mode

    if mode == "no_teacher":
        no_teacher = No_Teacher.No_teacher()
        if not config.test_mode:
            no_teacher.train()
        no_teacher.test()
    elif mode == "zero_shot":
        zeros = zero_shot.ZeroShot()
        zeros.train()
    elif mode == "kd_at":
        kd_at = KD_AT.FewShotKT()
        kd_at.train_KT_AT()
    else:
        raise ValueError('Not valid mode')




