df = read.csv('data.csv', header = TRUE, sep = ',')

ave = mean(df, na.rm = TRUE)
sort(ave, decreasing=TRUE)

cnt = sapply(df, function(x) length(which( is.na(x) == FALSE)))
sort(cnt, descending = TRUE)

cnt4 = sapply(df, function(x) length(which( x >= 4)))
p4 = cnt4 / cnt
sort(p4, decreasing = TRUE)

sw = df[,2]
swc = sapply(df, function(x) length(which( is.na(x+sw) == FALSE)))
swp = swc / cnt
sort(swp, decreasing = TRUE)
