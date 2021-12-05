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
        color: black;
        font-family: 'Do Hyeon', sans-serif;
    }
    section {
        background-color: #FDFCF0;
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
</style>
EOP

@cgvMovieName = ("듄", "엘칸토 - 마법의 세계", "연애 빠진 로맨스", "유체이탈자");
@cgvMoviePoster = (
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000084/84945/84945_1000.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85121/85121_1000.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85239/85239_1000.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000083/83105/83105_1000.jpg"
);
@cgvMovieLink = (
    "http://www.cgv.co.kr/movies/detail-view/?midx=84945",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85121",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85239",
    "http://www.cgv.co.kr/movies/detail-view/?midx=83105"
);
$movieCount = @cgvMovieName;

print "<section>";
print h2("CGV 무비차트");
print "<table cellspacing=30px>";

print "<tr>\n";
for ($i = 0; $i < $movieCount; $i++) {
    print "<td>\n<div class = poster>\n";
    print "<a href = \"@cgvMovieLink[$i]\" target = \"blank\"><img src = \"@cgvMoviePoster[$i]\"></a>\n";
    print "<p><a href = \"@cgvMovieLink[$i]\" target = \"blank\">@cgvMovieName[$i]</a></p>\n";
    print "</div>\n</td>\n";
}
print "</tr>\n";
print "</table></section>";
print end_html();
print "\n\n";