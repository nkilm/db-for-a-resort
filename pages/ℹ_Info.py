import streamlit as st

st.title("Database Information")

st.markdown("""
### `Customer`

| Field     | Type         | Null | Key | Default | Extra |
| ---       |    ---       | ---  | --- |  ---    |  ---  |
| cid       | decimal(4,0) | NO   | PRI | NULL    |       |
| fname     | varchar(20)  | YES  |     | NULL    |       |
| minit     | char(1)      | YES  |     | NULL    |       |
| lname     | varchar(20)  | YES  |     | NULL    |       |
| address   | varchar(30)  | YES  |     | NULL    |       |
| email     | varchar(30)  | YES  |     | NULL    |       |
| contactNo | varchar(15)  | YES  |     | NULL    |       |
| waiter_id | decimal(3,0) | YES  | MUL | NULL    |       |

---

### `Resort`
| Field         | Type         | Null | Key | Default | Extra |
| ---     | ---    | --- | ---    |     ---  | --- |
| resort_id     | decimal(4,0) | NO   | PRI | NULL    |       |
| resort_name   | varchar(50)  | NO   |     | NULL    |       |
| address       | varchar(40)  | NO   |     | NULL    |       |
| rating        | decimal(3,2) | YES  |     | NULL    |       |
| price_per_day | float        | YES  |     | NULL    |       |

""")