var daysUntilMyBirthday = 60;

for (var i = daysUntilMyBirthday; i >= 0; i-=1) {
    if (i >= 30) {
        console.log(i + " days until my birthday.  Such a long time... :(")
    } else if (i < 30 && i >= 5) {
        console.log(i + " Days Until My Birthday! :)");
    } else if (i > 1 && i < 5) {
        console.log(i + " DAYS UNTIL MY BIRTHDAY!!!");
    } else if (i === 1){
        console.log(i + " DAY UNTIL MY BIRTHDAY!!!");
    } else {
        console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*");
        console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪");
        console.log("*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");
    }
}
