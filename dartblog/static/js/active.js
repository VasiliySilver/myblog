$(document).ready(function () {

    // Для каждого пункта меню с тегом a
    $('.menu a').each(function () {
        // находим url страницы на которой находимся
        let location = window.location.protocol = '//' + window.location.host + window.location.pathname;
        // находим ссылку
        let link = this.href;
        // если локация равна ссылке добавляем класс active
        if (location == link) {
            $(this).parent().addClass('active')
        }
    })

    var filterFns = {
        numberGreaterThan50: function () {
            var number = $(this).find('.number').text();
            return parseInt(number, 10) > 50;
        },
        ium: function () {
            var name = $(this).find('.name').text();
            return name.match(/ium$/);
        }
    };
    $('.filters-button-group').on('click', 'button', function () {
        var filterValue = $(this).attr('data-filter');
        filterValue = filterFns[filterValue] || filterValue;
        $grid.isotope({
            filter: filterValue
        });
    });
    $('.button-group').each(function (i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });
});