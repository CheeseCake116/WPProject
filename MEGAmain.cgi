#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

print header("Content-type: text/html; charset=utf-8");
print "<head>\n";
print "<title>Untitled Document</title>";
print "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n";
print "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n";
print "<link href=\"https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap\" rel=\"stylesheet\">\n";
print <<EOP;
<style>
    * {
        margin: 0;
        padding: 0;
        text-align: center;
        color: white;
        font-family: 'Do Hyeon', sans-serif;
    }
    body {
        height : 1200px;
    }
    section {
        background-color: rgb(50, 33, 96);
        width: 100%;
        height: 100%;
    }
    h2 {
        padding: 20px;
        text-align : left;
        margin-left : 15%;
    }
    img {
        width: 200px;
    }
    table {
        margin: auto;
    }
    p {
        margin : 10px;
        font-size : 130%;
    }
    .poster:hover {
        opacity : 0.5;
    }
    .rank {
        background-color : rgb(25, 24, 51);
        color : white;
    }
</style>
EOP

@megaMovieName = (
    "킬링 카인드: 킬러의 수제자", "돈 룩 업", "태일이", "너에게 가는길",
    "유체이탈자", "고스트버스터즈 라이즈", "라스트 나잇 인 소호", "언힐러"    
);
@megaMoviePoster = (
    "https://img.megabox.co.kr/SharedImg/2021/11/19/OSwPwX3tSSnxJZMGljSs2tZESq6uFliO_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/12/02/E3UIW76SDtxGcGAOqHD7ZsXcJ0y856tf_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/12/02/j3wKuMLP0OjyE7PBNqDfcmzUGEtv9l9e_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/01/JSLiuBzfSh0944XsetBXVFZSSaXfPjO6_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/03/tP5BVdJ82rerjg37crDMrNpehEFcPfuZ_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/12/ZL6rOSUwTNgWJLdJ0RM58Y4IsVs8m77h_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/08/3ZcfD8ozZSG8r0uGKs1Aib4h7u6Gb0ZF_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/26/UgC0ynJIDkgMHevC4Z1c4isRIRsjsUMT_420.jpg",
);
@megaMovieLink = (
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21061000",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21086300",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21075400",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21073200",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21075100",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=01675700",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21077200",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21086000"
);
$movieCount = @megaMovieName;

print "<section>";
print h2("메가박스 무비차트");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=30px>";

open(IN, "movie.out");
@movies = <IN>;
close(IN);

print "<tr>\n";
for ($i = 0; $i < $movieCount; $i++) {
    $flag = 0;
    foreach $movie (@movies) {
        if (substr($movie, 0, 3) eq "meg" && substr($movie, 3, 1) eq $i) {
            $flag = 1;
        }
    }
    $r = $i + 1;
    print "<td>\n<p class = rank>No. $r</p>\n<div class = poster>\n";
    print "<a href = \"$megaMovieLink[$i]\" target = \"blank\"><img src = \"$megaMoviePoster[$i]\"></a>\n";
    print "<p><a href = \"$megaMovieLink[$i]\" target = \"blank\">$megaMovieName[$i]</a></p>\n</div>\n";
    if ($flag == 0) {
        print "<p style = \"text-align : right; font-size : 100%;\"><a href = \"movie.cgi?name=meg$i\">추가하기</a></p>\n";
    } else {
        print "<p style = \"font-size : 100%; text-align : right;\">이미 추가된 영화</p>"
    }
    print "</td>";
    
    if ($i == 3) { print "</tr><tr>"; 
    }
}
print "</tr>\n";
print "<tr><td colspan = '4' style = 'text-align : right;'><a href = 'https://www.megabox.co.kr/movie' target = 'blank'>더보기</a></td></tr>\n";
print "</table></section>";
print end_html();
print "\n\n";