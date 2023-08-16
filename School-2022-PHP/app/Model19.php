<?php

namespace app;
use mysqli;

class Model19
{
    protected $link;

    public function __construct()
    {
        $this->link = new MySQLi('localhost:3306', 'root', 'Taoymjsun24', 'php1');
        $this->link->set_charset('utf8mb4');
    }

    public function getAll()
    {
        $sql = 'SELECT * FROM `data1`';
        $res = $this->link->query($sql);
        return $res->fetch_all(MYSQLI_ASSOC);
    }
}
