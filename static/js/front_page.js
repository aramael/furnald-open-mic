/**
 * Created with PyCharm.
 * User: aramael
 * Date: 1/30/13
 * Time: 4:35 PM
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function(){

    spectrum();

    var timeout;
    var time = 20000;

    function spectrum(){

        var hue = 'rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';

        $('.coloured').animate( { backgroundColor: hue, color: hue }, time);

//        timeout = setTimeout( function(){
//            spectrum();
//        }, time);

    }

});