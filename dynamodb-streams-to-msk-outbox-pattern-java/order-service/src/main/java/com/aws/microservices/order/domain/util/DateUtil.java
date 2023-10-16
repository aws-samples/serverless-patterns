package com.aws.microservices.order.domain.util;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateUtil {

    public static String getFormattedDate(Date date) {

        SimpleDateFormat newFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        return newFormat.format(date);
    }

}
