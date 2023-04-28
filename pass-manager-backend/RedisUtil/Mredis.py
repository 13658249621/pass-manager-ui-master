import redis


class Mredis:
    """redis连接池"""

    def __init__(self) -> None:
        self.pool = redis.ConnectionPool(host='localhost', port=6379)
        self.conn = redis.Redis(connection_pool=self.pool)

    # 删除键
    def del_key(self, key):
        self.conn.delete(key)

    # 字符串添加
    def str_set(self, key, val):
        self.conn.set(key, val)

    # 字条串读取
    def str_get(self, key):
        return self.conn.get(key)

    # 字符串添加
    # 设置键值： name="alice" 且超时时间为10秒，(值写入到redis时会自动转字符串)
    # conn.set("name", "alice", ex=10)
    def str_time_set(self, key, val, time):
        self.conn.set(key, val, ex=time)

    # 列表
    # 从类别左侧进
    def l_push(self, key, value):
        self.conn.lpush(key, value)

    # 从列表右侧进
    def r_push(self, key, value):
        self.conn.rpush(key, value)

    # 列表长度
    def t_len(self, key):
        return self.conn.llen(key)

    # 从右侧移除一个元素并返回对应值
    def r_pop(self, key):
        return self.conn.rpop(key)

    # 获取列表中所有值
    def all_list(self, key):
        return self.conn.lrange(key, 0, -1)

    # 有侧开始删除n个值
    def rem_n_value(self, key, count, value):
        return self.conn.lrem(key, -count, value)

    # hash
    # 添加
    def hash_add(self, pkey, key, v):
        self.conn.hset(pkey, key, v)

    #     单个
    def hash_get(self, pkey, key):
        return self.conn.hget(pkey, key)

    #     获取所有
    def hash_getall(self, pkey):
        return self.conn.hgetall(pkey)

    #     hsetnx 给哈希表key添加field-value对，当且仅当域field不存在
    def hash_setnx(self, pkey, key, v):
        self.conn.hsetnx(pkey, key, v)

    #     jiajian 为哈希表key中的域field的值加上<incerment>
    def hash_jiajian(self, pkey, key, count):
        self.conn.hincrby(pkey, key, count)
        # 删除hash中的指定字段, 字段对应的值会一起删除

    def hsah_hdel(self, pkey, key):
        self.conn.hdel(pkey, key)

    #     setnx
    def str_setnx(self, key, v):
        return self.conn.setnx(key, v)

    def store_change(self, key, count, type):
        #         type1加 2减
        if type == 1:
            self.conn.decrby(key, count)
        else:
            self.conn.incrby(key, count)

    #     set
    def set_add(self, k, v):
        self.conn.sadd(k, v)

    def set_getall(self, k):
        return self.conn.smembers(k)

    def set_del(self, k):
        return self.conn.delete(k)


