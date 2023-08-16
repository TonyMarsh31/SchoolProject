package service;

import bean.Users;

public interface UsersService {
    /**
     * 登陆方法
     */
    public Users login(String username,String password);
}
