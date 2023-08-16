package dao;

import bean.Users;

public interface UsersDao {
    /**
     * 登陆方法
     */
    public Users login(String username, String password);
}
