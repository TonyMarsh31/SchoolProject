package dao;

import bean.Grade;

import java.util.List;

public interface GradeDao {
    /**
     * 查询年级列表
     * @return
     */
    public List<Grade> getList();
}