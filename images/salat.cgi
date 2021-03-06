
<!DOCTYPE html>
<html>
    <head>
        <title>Account Temporary On Hold</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Rubik:300,400" rel="stylesheet">
        <style>
            body{
                font-family: 'Rubik', sans-serif;
                font-size: 14px;
                font-weight: 300;
                margin: 0;
                padding: 0;
            }
            .page-wrapper{
                text-align: center;
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(to bottom right, #ffffff, #f6ead5);
            }
            .header-section{
                padding: 80px 20px 0;
                text-align: center;
                margin-bottom: 30px;
            }
            .header-section h3{
                font-weight: 300;
                font-size: 28px;
                margin: 10px 0;
                color: #856404;
            }
            .header-section i{
                font-size: 52px;
                color: #f7cc81;
            }
            .content{
                padding: 30px 20px;
                text-align: center;
                background: #fae0b3;
                color: #856404;
                margin-bottom: 30px;
            }
            .content p{
                font-size: 20px;
                line-height: 32px;
            }
            .content-holder{
                position: relative;
                top: 15%;
            }
            .sleeping-robot{
                color: #856404;
                font-size: 15px;
            }
            .sleeping-robot img{
                display: block;
                margin: 0 auto;
            }
            .sleeping-robot blockquote{
                display: inline-block;
                margin: 0px;
                text-align: right;
                width: 400px;
            }
            .sleeping-robot blockquote p{
                margin: 3px 0;
            }
            .sleeping-robot blockquote p:last-child{
                text-align: right;    
                margin: 5px 3px;
            }
            @media screen and (max-width: 991px){
                .header-section{
                    padding: 50px 0 0;
                }
                .content-holder{
                    top: 10%;
                }
                .content p > br{
                    display: none;
                }
            }
            @media screen and (max-width: 767px){
                .header-section{
                    padding: 20px 0 0;
                }
                .content-holder{
                    top: 0;
                }
                .content{
                    padding: 15px;
                    margin-bottom: 20px;
                }
                .header-section h3{
                    font-size: 22px;
                }
                .content p{
                    font-size: 15px;
                    line-height: 26px;
                    margin: 5px 0;
                }
                .page-wrapper img {
                    width: 70%;
                }
                .sleeping-robot{
                    font-size: 13px;
                }
                .sleeping-robot blockquote{
                    width: 70%;
                }
            }
        </style>
    </head>
    <body>
        <section class="page-wrapper">
            <div class="content-holder">
                <div class="header-section">
                    <i class="material-icons">pause_circle_outline</i>
                    <h3>
                        Account Temporary On Hold
                    </h3>
                </div>
                <div class="content">
                    <p>
                        This account is temporary On Hold. Please check your billing for outstanding invoices 
                        <br>
                        and the Report Center for any unaddressed Resource usage Incident Reports.
                    </p>
                </div>
                <div class="sleeping-robot">
                    <img src="https://cdn.fastcomet.com/icons/sleeping-robot.svg" width="400">
                    <blockquote>
                        <p><i>Do Androids Dream of Electric Sheep?</i></p>
                        <p>- Philip K. Dick</p>
                    </blockquote>
                </div>
            </div>
        </section>
    </body>
</html>
