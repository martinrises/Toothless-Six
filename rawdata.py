# -*- coding: utf-8 -*-
# Copyright 2017 The Xiaoyu Fang. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import pandas as pd
import os


class RawData(object):
    def __init__(self, date, open, high, close, low, volume):
        self.date = date
        self.open = open
        self.high = high
        self.close = close
        self.low = low
        self.volume = volume


def read_sample_data(path):
    print("reading histories...")
    raw_data = []
    df = pd.read_csv(path)
    for i in range(1, len(df.index)):
        raw_data.append(RawData(df.date[i], float(df.open[i]), float(df.high[i]), float(df.close[i]), float(df.low[i]),
                                float(df.volume[i])))
    sorted_data = sorted(raw_data, key=lambda x: x.date)
    print("got %s records." % len(sorted_data))
    return sorted_data


def generate_csv(path):
    if not os.path.isdir(path):
        exit(1)
    file_list = os.listdir(path)
    for f in file_list:
        file_path = os.path.join(path, f)
        raw_data = []
        separator = "\t"
        with open(file_path, "r") as fp:
            for line in fp:
                if line.startswith("date"):
                    continue
                l = line[:-1]
                fields = l.split(separator)
                if len(fields) > 5:
                    raw_data.append(
                        RawData(fields[0], float(fields[1]), float(fields[2]), float(fields[3]), float(fields[4]),
                                float(fields[5])))
        sorted_data = sorted(raw_data, key=lambda x: x.date)
        dates = [data.date for data in sorted_data]
        opens = [data.open for data in sorted_data]
        closes = [data.close for data in sorted_data]
        highs = [data.high for data in sorted_data]
        lows = [data.low for data in sorted_data]
        volumes = [data.volume for data in sorted_data]
        data_dict = {
            'date': dates,
            'open': opens,
            'close': closes,
            'high': highs,
            'low': lows,
            'volume': volumes
        }
        df = pd.DataFrame(data=data_dict)
        df.to_csv(os.path.join('/home/liuzhf/workspace/projects/age-recognition/Toothless-Sixth/dataset/debug', f))


if __name__ == '__main__':
    generate_csv('/home/liuzhf/workspace/projects/age-recognition/Toothless-Sixth/dataset/csv')
