

import os
import time

import redis

class RedisAPILimitCounter:    
    """Redis Counter"""
    def __init__(self, conn_redis, key=str, is_counter_reset=False, ex_time=1200, init_num=1, reqeust_limit=200):
        """
        
        
        Parameters
        ----------
        conn_redis : conn_redis:Redis<ConnectionPool<Connection>>
            redis connection object.
        key : str 
            redis key
        is_counter_reset : bool default False
            if True redis key's counter is initialized.
        ex_time : int default 1200 == 2 minutes
            set redis key's expire time.
            sey as your API_KEY limit time.
        init_num : int default 0
            initial number of redis key's count.
        reqeust_limit : int default 200
            API request limit.\n
            if your API-KEY is production level use 200. 
        """
        self.conn_redis = conn_redis
        self.key  = key
        self.ex_time = ex_time
        self.request_limit = reqeust_limit
        if isinstance(init_num, int) is False:
            raise Exception("init_num must be integer data type")             
        self.init_num = init_num
        
        if is_counter_reset is True:
            self.conn_redis.setex(name=self.key, time=self.ex_time, value=init_num)

    def plus(self, int_plus_num=1, is_error_reset=True):
        """
          카운터에 정수형 숫자(기본:1)를 더한 숫자를 리턴한다
          :param int_plus_num:int: 정수형 숫자
          :param is_error_reset:bool: 오류발생시 카운터를 초기값으로 리셋여부
          :return counter_number:int: 더해진 최종 카운터 값
        """
        if isinstance(int_plus_num, int) is False:
            raise Exception("int_plus_num must be integer data type")
        try:
            key_exists = self.exists()
            if key_exists == 1 :
                api_counter = self.get()
                if api_counter >= (self.request_limit-1) :
                    os.system(f'echo "Your requests are going to limit.\nBegin Time Sleep for 1200 seconds."')
                    time.sleep(self.ex_time)
                    self.conn_redis.setex(name=self.key, time=self.ex_time, value=self.init_num)
                
                return int(self.conn_redis.incr(name=self.key, amount=int_plus_num))
            else:
                self.conn_redis.setex(name=self.key, time=self.ex_time, value=self.init_num)
                return
            # INCR COMMAND: Time complexity: O(1)
            
        except redis.ResponseError: # 값이 숫자가 아니거나 64비트 부호정수형 범위를 넘어간 경우
            if is_error_reset is True:
                self.conn_redis.set(name=self.key, value=self.init_num) # 초기값으로 설정한다
                return self.init_num # 초기값을 반환한다
            else:
                pass
    def get(self):
        """ :return counter_number:int: 현재 카운터 값"""
        return int(self.conn_redis.get(name=self.key))

    def reset(self):
        """"reset count"""
        self.conn_redis.setex(name=self.key, time=self.ex_time , value=self.init_num)
    
    # @classmethod
    def exists(self):
        """
        returns if your key exists
        
        Returns 1 or 0
        --------------
        1 : exists
        0 : no exists
        """
        return self.conn_redis.exists(self.key)