#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

print header("Content-type: text/html; charset=utf-8");
print "\n";
print start_html();
# print "<!DOCTYPE html>";
print "\n";
print "<head>\n";
print "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n";
print  "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n";
print "<link href=\"https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap\" rel=\"stylesheet\">\n";
print "</head>\n";

print <<EOP;
<style>
    * {
        margin: 0;
        padding: 0;
        text-align: center;
        color: white;
        font-family: 'Do Hyeon', sans-serif;
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
</style>
EOP

@megaMovieName = ("킬링 카인드: 킬러의 수제자", "돈 룩 업", "유체이탈자", "고스트버스터즈 라이즈");
@megaMoviePoster = (
    "https://img.megabox.co.kr/SharedImg/2021/11/19/OSwPwX3tSSnxJZMGljSs2tZESq6uFliO_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/12/02/E3UIW76SDtxGcGAOqHD7ZsXcJ0y856tf_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/03/tP5BVdJ82rerjg37crDMrNpehEFcPfuZ_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/12/ZL6rOSUwTNgWJLdJ0RM58Y4IsVs8m77h_420.jpg"
);
@megaMovieLink = (
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21061000",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21086300",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21075100",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=01675700"
);
$movieCount = @megaMovieName;

print "<section>";
print h2("메가박스 무비차트");
print "<table cellspacing=30px>";
print "<tr>\n";
for ($i = 0; $i < $movieCount; $i++) {
    print "<td>\n<div class = poster>\n";
    print "<a href = \"@megaMovieLink[$i]\" target = \"blank\"><img src = \"@megaMoviePoster[$i]\"></a>\n";
    print "<p><a href = \"@megaMovieLink[$i]\" target = \"blank\">@megaMovieName[$i]</a></p>\n";
    print "</div>\n</td>\n";
}
print "</tr>\n";
print "</table></section>";
print end_html();
print "\n\n";