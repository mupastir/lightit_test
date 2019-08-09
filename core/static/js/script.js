function cipher() {
            $.ajax({
                type: "POST",
                url: "/cipher",
                data: $('form').serialize(),
                success: function(response) {
                    var json = jQuery.parseJSON(response)
                    var ctx = document.getElementById('Diagram').getContext('2d');
                    var Diagram = new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: Object.keys(json.frequency_rough),
                            datasets: [{
                                label: 'Letters in given text',
                                data: Object.values(json.frequency_rough),
                                backgroundColor: "rgba(0,147,68,0.2)",
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                        beginAtZero: true
                                    }
                                }]
                            }
                        }
                    });
                    $('#result').html(json.result)
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }