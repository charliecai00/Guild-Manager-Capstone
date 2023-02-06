import React from "react";
import './Warfield.css';
import { Link } from "react-router-dom";

const Warfield = () => {
  return (
    <div>

<head>
    <meta charset="utf-8" />
    <title>Fight</title>
    <meta content="Fight" property="og:title" />
    <meta content="Fight" property="twitter:title" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <meta content="Webflow" name="generator" />
    <link href="./warfield.css"
        rel="stylesheet" type="text/css" />
    <link href="https://fonts.googleapis.com" rel="preconnect" />
    <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="anonymous" />
    <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
    <link href="https://uploads-ssl.webflow.com/img/favicon.ico" rel="shortcut icon" type="image/x-icon" />
    <link href="https://uploads-ssl.webflow.com/img/webclip.png" rel="apple-touch-icon" />
</head>

<body class="body">
    <section class="features-table wf-section">
        <div data-animation="default" data-collapse="medium" data-duration="400" data-easing="ease" data-easing2="ease"
            role="banner" class="navbar w-nav">
            <div class="container-5 w-container"><a href="#" class="brand w-nav-brand"><img
                        src="https://uploads-ssl.webflow.com/63dd34e66ca34e4b9f4199d7/63de9aa447ab585d1895c3fb_logo.png"
                        loading="lazy" width="66" alt="" /></a>
                <nav role="navigation" class="w-nav-menu">
                    <Link to="/" aria-current="page" class="nav-link w-nav-link w--current">Home</Link>
                    <Link to="/warfield" class="nav-link-2 w-nav-link">WarField</Link>
                </nav>
                <div class="w-nav-button">
                    <div class="w-icon-nav-menu"></div>
                </div>
            </div>
        </div>
    </section>
    <div class="w-layout-grid grid-5">
        <div data-current="Tab 1" data-easing="ease" data-duration-in="300" data-duration-out="100"
            class="tabs-2 w-tabs">
            <div class="w-tab-menu"><a data-w-tab="Tab 1" class="tab-link-tab-1-2 w-inline-block w-tab-link w--current">
                    <div>Party1</div>
                </a><a data-w-tab="Tab 2" class="tab-link-tab-2-3 w-inline-block w-tab-link">
                    <div>Party2</div>
                </a><a data-w-tab="Tab 3" class="tab-link-tab-3-2 w-inline-block w-tab-link">
                    <div>Party3</div>
                </a></div>
            <div class="w-tab-content">
                <div data-w-tab="Tab 1" class="w-tab-pane w--tab-active">
                    <p id="w-node-bb97bd61-e036-f759-3fd8-f22e917474f1-6639e95d" class="paragraph-2">Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis
                        cursus, mi quis viverra ornare, eros d </p><a
                        id="w-node-_46a6ce26-088c-f0a0-cf29-2caf60a34c51-6639e95d" href="#" class="w-button">Choose</a>
                </div>
                <div data-w-tab="Tab 2" class="w-tab-pane"></div>
                <div data-w-tab="Tab 3" class="w-tab-pane"></div>
            </div>
        </div>
        <div data-delay="4000" data-animation="slide" class="slider-2 w-slider" data-autoplay="false" data-easing="ease"
            data-hide-arrows="false" data-disable-swipe="false" data-autoplay-limit="0" data-nav-spacing="3"
            data-duration="500" data-infinite="true" id="w-node-_85c1b682-385d-e61d-14c6-800c43ea3a6b-6639e95d">
            <div class="w-slider-mask">
                <div class="slide w-slide"></div>
                <div class="slide-2 w-slide"></div>
                <div class="w-slide"></div>
            </div>
            <div class="w-slider-arrow-left">
                <div class="w-icon-slider-left"></div>
            </div>
            <div class="w-slider-arrow-right">
                <div class="w-icon-slider-right"></div>
            </div>
            <div class="w-slider-nav w-round"></div>
        </div>
    </div>
    <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=63dd34e66ca34e4b9f4199d7"
        type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
        crossorigin="anonymous"></script>
    <script src="https://uploads-ssl.webflow.com/63dd34e66ca34e4b9f4199d7/js/webflow.942be9691.js"
        type="text/javascript"></script>
</body>

    </div>
  );
};
  
export default Warfield;