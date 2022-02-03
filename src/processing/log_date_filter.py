class LogDateFilter:
    """
    Filter out logs based on date.
    """

    def filter_cookies(cookies, datestamps, desired_date):
        """
        Filters given cookies and datestamps data and keeps only cookies with desired date.
        
        Args:
            cookies         Cookies to be filtered. (The order has to match the order of corresponding datestamps.)
            datestamps      Datestamps information for given cookies. (Expects sorted datestamps.)
            desired_date    Desired date whose cookies should be kept in the filtered results.

        Returns:
            Cookies (with duplicates) with the desired date.
        """

        cookies_cnt = len(cookies)

        if cookies_cnt != len(datestamps):
            raise ValueError('Number of cookies and datestamps do not match.')

        filtered_cookies = []

        data_idx = 0
        while data_idx < cookies_cnt:
            if datestamps[data_idx].startswith(desired_date):
                while data_idx < cookies_cnt and datestamps[data_idx].startswith(desired_date):
                    filtered_cookies.append(cookies[data_idx])
                    data_idx += 1

                return filtered_cookies

            data_idx += 1

        return filtered_cookies
