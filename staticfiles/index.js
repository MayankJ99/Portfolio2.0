    document.addEventListener('DOMContentLoaded', function () {
        var elems = document.querySelectorAll('.sidenav');
        var instances = M.Sidenav.init(elems, {edge: 'right'});
    });

    $(document).ready(function () {
        $('.modal').modal();
    });

    $(document).ready(function () {
        $('.scrollspy').scrollSpy();
    });
    $(document).ready(function () {
        $('.materialboxed').materialbox();
    });

    document.addEventListener('DOMContentLoaded', function () {
        var elems = document.querySelectorAll('.fixed-action-btn');
        var instances = M.FloatingActionButton.init(elems, {
            hoverEnabled: false
        });
    });
    AOS.init();
