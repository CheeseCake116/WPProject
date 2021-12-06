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
        color : black;
        font-family: 'Do Hyeon', sans-serif;
    }
    body {
        height : 1200px;
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

@lotteMovieName = (
    "유체이탈자", "연애 빠진 로맨스", "엔칸토: 마법의 세계", "고스트버스터즈 라이즈",
    "듄", "베네데타", "이터널스", "라스트 나잇 인 소호"
);
@lotteMoviePoster = (
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18093_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18081_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18041_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202007/15368_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202110/17864_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18064_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/17885_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202112/18156_103_1.jpg"
);
@lotteMovieLink = (
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18093",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18081",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18041",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=15368",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=17864",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18064",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=17885",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18156"
);
$movieCount = @lotteMovieName;

print "<section>";
print h2("롯데시네마 무비차트");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=30px>";

open(IN, "movie.out");
@movies = <IN>;
close(IN);

print "<tr>\n";
for ($i = 0; $i < $movieCount; $i++) {
    $flag = 0;
    foreach $movie (@movies) {
        if (substr($movie, 0, 3) eq "lot" && substr($movie, 3, 1) eq $i) {
            $flag = 1;
        }
    }
    $r = $i + 1;
    print "<td>\n<p class = rank>No. $r</p>\n<div class = poster>\n";
    print "<a href = \"$lotteMovieLink[$i]\" target = \"blank\"><img src = \"$lotteMoviePoster[$i]\"></a>\n";
    print "<p><a href = \"$lotteMovieLink[$i]\" target = \"blank\">$lotteMovieName[$i]</a></p>\n</div>\n";
    if ($flag == 0) {
        print "<p style = \"text-align : right; font-size : 100%;\"><a href = \"movie.cgi?name=lot$i\">추가하기</a></p>\n";
    } else {
        print "<p style = \"font-size : 100%; text-align : right;\">이미 추가된 영화</p>"
    }
    print "</td>";
    
    if ($i == 3) { print "</tr><tr>"; 
    }
}
print "</tr>\n";
print "<tr><td colspan = '4' style = 'text-align : right;'><a href = 'https://www.lottecinema.co.kr/NLCHS/Movie/List?flag=1' target = 'blank'>더보기</a></td></tr>\n";
print "</table></section>";
print end_html();
print "\n\n";