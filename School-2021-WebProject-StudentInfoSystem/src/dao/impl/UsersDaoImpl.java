package dao.impl;

import bean.Users;
import util.DBUtils;
import dao.UsersDao;

import java.sql.SQLException;
import java.util.ArrayList;

public class UsersDaoImpl extends DBUtils implements UsersDao {
    @Override
    public Users login(String username, String password) {
        Users users = null;
        try {
            String sql = "select * from users where loginname=? and password=?";
            ArrayList arrayList = new ArrayList();
            arrayList.add(username);
            arrayList.add(password);
            resultSet = query(sql, arrayList);
            if (resultSet == null){
                return null;
            }
            while (resultSet.next()) {
                users = new Users();
                users.setLoginName(username);
                users.setRealName(resultSet.getString("realname"));
                users.setUserId(resultSet.getInt("userid"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }

        return users;
    }
}
