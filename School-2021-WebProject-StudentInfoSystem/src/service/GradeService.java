package service;

import bean.Grade;

import java.util.List;

public interface GradeService {
    /**
     * 查询年级列表
     * @return
     */
    public List<Grade> getList();
}
