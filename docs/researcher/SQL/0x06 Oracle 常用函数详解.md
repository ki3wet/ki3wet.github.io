# Oracle 常用函数详解与实战

---

## 一、函数分类概述

Oracle 中的函数可以分为以下几类：

- **聚合函数**：如 `MAX`, `MIN`, `AVG`, `SUM`, `COUNT`
- **转换函数**：如 `NVL`, `TO_CHAR`, `TO_DATE`, `COALESCE`
- **单行函数**：
  - 数字函数
  - 字符函数
  - 日期函数

---

## 二、聚合函数

| 函数名 | 说明 | 示例 |
|--------|------|------|
| `MAX()` | 取最大值 | `SELECT MAX(SAL) FROM EMP;` |
| `MIN()` | 取最小值 | `SELECT MIN(SAL) FROM EMP;` |
| `AVG()` | 取平均值 | `SELECT AVG(SAL) FROM EMP;` |
| `SUM()` | 求和 | `SELECT SUM(SAL) FROM EMP;` |
| `COUNT()` | 统计行数或非空值 |
| `COUNT(1)` | 统计所有行（包括空值） | `SELECT COUNT(1) FROM EMP;` |
| `COUNT(字段)` | 统计非空字段 | `SELECT COUNT(COMM) FROM EMP;` |

---

## 三、转换函数

### 1. 空值处理函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `NVL(X, Y)` | 如果 X 为 NULL，则返回 Y | `SELECT NVL(COMM, 0) FROM EMP;` |
| `NVL2(X, Y, Z)` | 如果 X 不为 NULL，返回 Y；否则返回 Z | `SELECT NVL2(COMM, '有奖金', '无奖金') FROM EMP;` |
| `COALESCE(X, Y, Z, ...)` | 返回第一个非空表达式 | `SELECT COALESCE(COMM, BONUS, 0) FROM EMP;` |

### 2. 类型转换函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `TO_DATE(字符串, 格式)` | 转换为日期 | `TO_DATE('20250715', 'YYYYMMDD')` |
| `TO_CHAR(日期/数字, 格式)` | 转换为字符串 | `TO_CHAR(SYSDATE, 'YYYY-MM-DD')` |
| `TO_NUMBER(字符串)` | 转换为数字 | `TO_NUMBER('123')` |
| `CAST(字段 AS 类型)` | 强制类型转换 | `CAST('123' AS NUMBER)` |

---

## 四、单行函数

---

### 1. 数字函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `ABS(X)` | 绝对值 | `SELECT ABS(-3.14) FROM DUAL;` → `3.14` |
| `ROUND(X, Y)` | 四舍五入 | `SELECT ROUND(3.1415, 2) FROM DUAL;` → `3.14` |
| `TRUNC(X, Y)` | 截断 | `SELECT TRUNC(3.1415, 2) FROM DUAL;` → `3.14` |
| `POWER(X, Y)` | 求幂 | `SELECT POWER(2, 3) FROM DUAL;` → `8` |
| `MOD(X, Y)` | 取余 | `SELECT MOD(7, 3) FROM DUAL;` → `1` |
| `CEIL(X)` | 向上取整 | `SELECT CEIL(2.1) FROM DUAL;` → `3` |
| `FLOOR(X)` | 向下取整 | `SELECT FLOOR(2.9) FROM DUAL;` → `2` |

#### ✅ 实战练习

```sql
-- 8.65 显示为 8
SELECT TRUNC(8.65), FLOOR(8.65) FROM DUAL;

-- 6.23 显示为 6.2
SELECT TRUNC(6.23,1), ROUND(6.23,1) FROM DUAL;

-- 3.61 显示为 4
SELECT ROUND(3.61), CEIL(3.61) FROM DUAL;
```

---

### 2. 日期函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `SYSDATE` | 当前系统日期 | `SELECT SYSDATE FROM DUAL;` |
| `ADD_MONTHS(X, Y)` | 增加月份 | `SELECT ADD_MONTHS(SYSDATE, 1) FROM DUAL;` |
| `MONTHS_BETWEEN(X, Y)` | 两个日期相差月数 | `SELECT MONTHS_BETWEEN(SYSDATE, HIREDATE) FROM EMP;` |
| `LAST_DAY(X)` | 返回当月最后一天 | `SELECT LAST_DAY(SYSDATE) FROM DUAL;` |
| `ROUND(X, 'YYYY')` | 四舍五入到年 | `SELECT ROUND(SYSDATE, 'YYYY') FROM DUAL;` |
| `TRUNC(X, 'MM')` | 截取到月 | `SELECT TRUNC(SYSDATE, 'MM') FROM DUAL;` |

#### ✅ 实战练习

```sql
-- 第三季度第一个月15号是星期几
SELECT TO_CHAR(ADD_MONTHS(TRUNC(SYSDATE, 'YYYY'), 6) + 14, 'DAY') FROM DUAL;

-- 去年今天上个月的月末
SELECT LAST_DAY(ADD_MONTHS(SYSDATE, -13)) FROM DUAL;

-- 3个月前的月末往前推10天
SELECT LAST_DAY(ADD_MONTHS(SYSDATE, -3)) - 10 FROM DUAL;

-- 员工入职到今天领取了多少个月工资
SELECT ENAME, FLOOR(MONTHS_BETWEEN(SYSDATE, HIREDATE)) AS 月数
FROM EMP;
```

---

### 3. 字符函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `REPLACE(X, Y, Z)` | 替换字符 | `SELECT REPLACE('2025-07-08', '-', '/') FROM DUAL;` |
| `LENGTH(X)` | 字符长度 | `SELECT LENGTH('我爱SING') FROM DUAL;` → `8` |
| `LENGTHB(X)` | 字节长度 | `SELECT LENGTHB('我爱SING') FROM DUAL;` → `10` |
| `TRIM(X)` | 去除空格 | `SELECT TRIM('   SING   ') FROM DUAL;` → `SING` |
| `LPAD(X, Y, Z)` | 左填充 | `SELECT LPAD('123', 5, '0') FROM DUAL;` → `00123` |
| `RPAD(X, Y, Z)` | 右填充 | `SELECT RPAD('123', 5, '0') FROM DUAL;` → `12300` |
| `SUBSTR(X, Y, Z)` | 截取字符串 | `SELECT SUBSTR('ABCDEFG', 3, 2) FROM DUAL;` → `CD` |
| `INSTR(X, Y, Z, M)` | 查找位置 | `SELECT INSTR('AHIANNAJKSDIANANIFJENLF', 'AN', 1, 2) FROM DUAL;` → `6` |
| `UPPER(X)` | 大写 | `SELECT UPPER('abc') FROM DUAL;` → `ABC` |
| `LOWER(X)` | 小写 | `SELECT LOWER('ABC') FROM DUAL;` → `abc` |
| `CONCAT(X, Y)` | 拼接字符串 | `SELECT CONCAT('Hello', ' World') FROM DUAL;` → `Hello World` |
| `||` | 管道拼接 | `'Hello' || ' ' || 'World'` → `Hello World` |
| `WM_CONCAT(X)` | 行转列拼接 | `SELECT DEPTNO, WM_CONCAT(ENAME) FROM EMP GROUP BY DEPTNO;` |

#### ✅ 实战练习

```sql
-- 查询员工信息表中名字不包含 A 的员工
SELECT * FROM EMP WHERE INSTR(ENAME, 'A') = 0;

-- 输出格式：SMITH的工资为1100元
SELECT ENAME || '的工资为' || SAL || '元' FROM EMP;
SELECT CONCAT(CONCAT(ENAME, '的工资为'), CONCAT(SAL, '元')) FROM EMP;
```

---

## 五、哈希与取模

| 函数 | 说明 | 示例 |
|------|------|------|
| `MOD(X, Y)` | 取模 | `SELECT MOD(10, 3) FROM DUAL;` → `1` |

可用于：

- 分布式数据分片
- 数据哈希后取模
- 轮询任务分配等

---

## 六、迁移与兼容性注意事项

| 问题 | 说明 | 解决方案 |
|------|------|----------|
| 日期格式差异 | DB2：`20250715` vs OB：`2025-07-15` | 使用 `TO_CHAR` / `TO_DATE` 统一格式 |
| 字符编码差异 | ORACLE：2字节中文 vs 高斯：3字节中文 | 扩展字段长度，避免字段超长 |
| 字符串拼接 | `||` vs `CONCAT()` | 优先使用 `||`，兼容性更好 |
| 行转列 | `WM_CONCAT()` | 可替换为 `LISTAGG()`（Oracle 11g+） |

---

## 七、示例总结

```sql
-- 查询员工工资信息
SELECT ENAME || '的工资为' || SAL || '元' AS 工资信息 FROM EMP;

-- 查询员工入职月数
SELECT ENAME, FLOOR(MONTHS_BETWEEN(SYSDATE, HIREDATE)) AS 入职月数 FROM EMP;

-- 查询第三季度第一个月15号星期几
SELECT TO_CHAR(ADD_MONTHS(TRUNC(SYSDATE, 'YYYY'), 6) + 14, 'DAY') FROM DUAL;
```

