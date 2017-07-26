/**
 * Created by root on 17-1-19.
 */


function people() {
    
}

people.prototype.hello = function () {
    document.write('hello,world!')
};

function stu() {
    
}


stu.prototype = new people();      //继承people

var s = new stu();
s.hello();