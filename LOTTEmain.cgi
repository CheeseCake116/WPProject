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
        font-family: 'Do Hyeon', sans-serif;
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
    .poster:hover {
        opacity : 0.5;
    }
</style>
EOP

@lotteMovieName = ("연애 빠진 로맨스", "유체이탈자", "돈 룩 업", "엔칸토: 마법의 세계");
@lotteMoviePoster = (
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18081_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18093_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202112/18309_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18041_103_1.jpg"
);
@lotteMovieLink = (
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18081",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18093",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18309",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18041"
);
$movieCount = @lotteMovieName;

print "<section>";
print h2("롯데시네마 무비차트");
print "<table cellspacing=30px>";
print "<tr>\n";
for ($i = 0; $i < $movieCount; $i++) {
    print "<td>\n<div class = poster>\n";
    print "<a href = \"@lotteMovieLink[$i]\" target = \"blank\"><img src = \"@lotteMoviePoster[$i]\"></a>\n";
    print "<p><a href = \"@lotteMovieLink[$i]\" target = \"blank\">@lotteMovieName[$i]</a></p>\n";
    print "</div>\n</td>\n";
}
print "</tr>\n";
print "</table></section>";
print end_html();
print "\n\n";