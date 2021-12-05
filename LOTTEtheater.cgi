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
        background-color: white;
        width: 100%;
        height: 100%;
    }
    h2 {
        padding: 20px;
    }
    td {
        text-align : left;
    }
    table {
        width : 70%;
        margin : auto;
    }
    td {
        padding : 10px;
        text-align : left;
        background-color : rgba(0, 0, 0, 0);
    }
    td:hover {
        background-color : rgba(0, 0, 0, 0.2);
    }
</style>
EOP

@lotteTheater = (
    "롯데시네마 대구광장", "롯데시네마 대구율하", "롯데시네마 대구현풍", "롯데시네마 동성로", "롯데시네마 프리미엄만경", 
    "롯데시네마 성서", "롯데시네마 프리미엄칠곡", "롯데시네마 상인"
);
@lotteTheaterLink = (
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=5012",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=5006",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=9076",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=5005",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=5004",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=5004",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=9057",
    "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=5&cinemaID=5016"
);

$theaterCount = @lotteTheater;

print "<section>\n";
print h2("롯데시네마 극장 (대구)");
print "<table cellspacing=20px>\n";
for ($i = 0; $i < $theaterCount; $i++) {
    print "<tr>\n<td><a href = \"@lotteTheaterLink[$i]\" target = \"blank\">@lotteTheater[$i]</a></td>\n</tr>\n";
}
print "</table>\n</section>\n";
print end_html();
print "\n\n";