<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>图书列表</title>
</head>
<body>
<table>
    <tr>
        <th>ID编号</th>
        <th>作者</th>
        <th>书名</th>
        <th>出版社</th>
    </tr>
    <?php foreach ($data as $row): ?>
        <tr>
            <td><?= $row['id'] ?></td>
            <td><?= $row['Author'] ?></td>
            <td><?= $row['Book'] ?></td>
            <td><?= $row['Publisher'] ?></td>
        </tr>
    <?php endforeach; ?>
</table>
</body>
</html>
