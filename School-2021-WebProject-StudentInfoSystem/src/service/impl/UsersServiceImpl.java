package service.impl;

import bean.Users;
import dao.UsersDao;
import dao.impl.UsersDaoImpl;
import service.UsersService;

public class UsersServiceImpl implements UsersService {
    private UsersDao usersDao = new UsersDaoImpl();

    @Override
    public Users login(String username, String password) {
        return usersDao.login(username,password);
    }
}
