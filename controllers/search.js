exports.index = function (req, res, next) {
  var q = req.query.q;
  q = encodeURIComponent(q);
  //res.redirect('https://www.google.com.hk/#hl=zh-CN&q=site:clickhouse.com.cn+' + q);
  res.redirect('https://cn.bing.com/search?q=site:clickhouse.com.cn+' + q);
};
