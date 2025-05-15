import json
import requests
import datetime
import argparse
import os
import pymysql
import time
from typing import Dict, List, Any

# 默认配置
DEFAULT_CONFIG = {
    "token": "**********",  # 隐藏敏感信息
    "company_id": "**********",  # 隐藏敏感信息
    "days_back": 2,
    "pol_cd": "CNXMN",
    "pod_cd": "VNVUT",
    "weeks_out": "6",
    "is_transit": "0",
    "db_host": "localhost",
    "db_port": 3306,
    "db_user": "root",
    "db_password": "",
    "db_name": "shipping_project",
    "db_charset": "utf8mb4"
}
