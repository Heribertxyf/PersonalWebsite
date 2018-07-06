function ResizeImage(_image, max_width, max_height) {
    //var max_width = 300;
    //var max_height = 300;
    var _width = _image.width;
    var _height = _image.height;
    var width_ratio = _width / max_width;
    var height_ratio = _height / max_height;
    //alert("Width ratio:" + width_ratio + ", Height Ratio:" + height_ratio);

    if ( width_ratio >= height_ratio && _image.width > max_width) {
        _image.width = max_width;
    }
    else if (height_ratio > width_ratio && _image.height > max_height) {
        _image.height = max_height;
    }
}