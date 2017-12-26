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
    df = pd.read_csv(path, names=['date', 'open', 'close', 'high', 'low', 'total_turnover', 'volume'])
    for i in range(1, len(df.index)):
        raw_data.append(RawData(df.date[i], float(df.open[i]), float(df.high[i]), float(df.close[i]), float(df.low[i]),
                                float(df.volume[i])))
    sorted_data = sorted(raw_data, key=lambda x: x.date)
    print("got %s records." % len(sorted_data))
    return sorted_data
