import pymysql


def get_conn():
    # 获取MYSQL的链接
    return pymysql.connect(
        host='localhost',
        user='root',
        password='lc040728',
        database='nurtuist',
        charset='utf8'
    )


def query_data(sql):
    # 查询信息，已弃用
    conn = get_conn()
    try:
        cursor = conn.cursor()  # 游标
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()


def select_date(data):
    # 查找姓名、密码对应的用户
    conn = get_conn()
    sql = """
    SELECT username, password FROM user
    WHERE username = %s
    AND password = %s
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchone()
        return result
    finally:
        conn.close()


def insert_name(data):
    # 注册
    sql_1 = """
        INSERT INTO 
        user(username,password) 
        VALUES(%s, %s);
    """
    sql_t = """
        SELECT id, username FROM user
        WHERE username = %s
        AND password = %s
    """
    sql_2 = """
        INSERT INTO 
        info(id,username) 
        VALUES(%s, %s);
    """
    sql_3 = """
        INSERT INTO 
        diet(id,username) 
        VALUES(%s, %s);
    """
    conn = get_conn()
    try:
        print("?")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_1, data)
        cursor.execute(sql_t, data)
        print("success")
        d1 = cursor.fetchone()
        d = (d1['id'], d1['username'])
        print(d)
        cursor.execute(sql_2, d)
        cursor.execute(sql_3, d)
        conn.commit()
    finally:
        conn.close()


def update(data, data_2):
    # 更新已存在用户的数据
    sql_1 = """
        UPDATE info SET sex=%s, age=%s, weight=%s, height=%s, body_fat_rate=%s, blood_sugar=%s, food_preference=%s
        WHERE username=%s;
    """
    sql_2 = """
        UPDATE diet SET Monday=%s, Tuesday=%s, Wednesday=%s, Thursday=%s, 
        Friday=%s, Saturday=%s, Sunday=%s 
        WHERE username=%s;
    """
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_1, data)
        cursor.execute(sql_2, data_2)
        conn.commit()
    finally:
        conn.close()


def select_food(data):
    # 查找对应用户的食谱
    conn = get_conn()
    sql = """
        SELECT Monday, Tuesday, Wednesday, Thursday,
        Friday, Saturday, Sunday FROM diet WHERE username = %s
        """
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, data)
        result = cursor.fetchone()
        return result
    finally:
        conn.close()


def create_db(table_name):
    # 创建数据库，初始化数据库时使用
    table_schema_1 = """
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,  -- 建议使用hash后的密码存储，并且考虑加盐
            pos VARCHAR(100)
        )
        """
    table_schema_2 = """
        CREATE TABLE IF NOT EXISTS info (
            id INT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            sex VARCHAR(10),
            age INT,
            height DECIMAL(5,2),   -- 身高可以是小数，所以用DECIMAL类型
            weight DECIMAL(6,2),   -- 体重也可以是小数
            body_fat_rate DECIMAL(6, 2),  -- 体脂率通常也是小数
            blood_sugar DECIMAL(6, 2),  -- 血糖值可能也需要支持小数
            food_preference TEXT  -- 食物偏好可以是文本描述，如果需要更结构化的数据，可考虑其他方式如JSON或关联其他表
        )
    """
    table_schema_3 = """
        CREATE TABLE IF NOT EXISTS diet (
            id INT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            Monday TEXT,  -- 食谱同理，可以用TEXT类型存储，复杂情况下也可以关联其他表
            Tuesday TEXT,
            Wednesday TEXT,
            Thursday TEXT,
            Friday TEXT,
            Saturday TEXT,
            Sunday TEXT
        )
    """
    table_schema_4 = """
   
        """
    # 创建数据库
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        check_sql = f"SHOW TABLES LIKE '{table_name}'"
        cursor.execute(check_sql)
        if cursor.fetchone() is None:
            cursor.execute(table_schema_1)
            cursor.execute(table_schema_2)
            cursor.execute(table_schema_3)
            cursor.execute(table_schema_4)
        conn.commit()
    finally:
        conn.close()


def main():
    table_name = "user"
    create_db(table_name)


if __name__ == '__main__':
    main()
