$(document).ready(function(){
    $('#menu').click(function(){
        $(this).toggleClass('fa-times');
        $('header').toggleClass('toggle');
    });
    $(window).on('scroll load', function(){
        $('#menu').removeClass('fa-times');
        $('header').removeClass('toggle');


        if($(window).scrollTop() > 0){
            $('.top').show();
        }else{
            $('.top').hide();
        }
    });

    // Smooth Scrolling

    $('a[href=""]').on('click',function(e){
      e.preventDefault();
 
      $('html, body').animate({

        scrollTop : $($(this),attr('href')).offset().top,
      },
        500,
        'linear'
      );

    });
    let valueDisplays = document.querySelectorAll(".num");
    let interval = 4000;

    valueDisplays.forEach(valueDisplay => {
        let startValue = 0;
        let endValue = parseInt(valueDisplay.getAttribute("data-val"));
        
        let duration = Math.floor(interval / endValue);

        let counter = setInterval(function(){
            startValue += 1;
            valueDisplay.textContent = startValue;

            if(startValue == endValue){
                clearInterval(counter);
            }
        }, duration)
    });

    
});

