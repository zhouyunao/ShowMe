// var list = [[10, 30], [23, 45], [65, 30], [67, 98]];
var list = {{schedule}}
var tbl = d3.select("#result")  // div#result内に出力
    .append("table")    // table要素を追加
    .selectAll("tr")    // tr要素を対象にする
    .data(list) // 出力するデータ
    .enter()    // データ数だけ要素を生成
    .append("tr")
    .selectAll("td")
    .data(function(row){    // 1行ごとにデータを返す
        return d3.entries(row); // key, valueを返す
    })
    .enter()
    .append("td")   // td要素を追加
    .text(function(d){
        return d.value; // valueが配列要素の値
    })
