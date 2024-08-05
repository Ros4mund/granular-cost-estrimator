import pandas as pd


def load_dataset(dir_path):
    data = dict()
    data["call_center"] = pd.read_csv(dir_path + '/call_center.csv', header=None)
    data["catalog_page"] = pd.read_csv(dir_path + '/catalog_page.csv', header=None)
    data["catalog_returns"] = pd.read_csv(dir_path + '/catalog_returns.csv', header=None)
    data["catalog_sales"] = pd.read_csv(dir_path + '/catalog_sales.csv', header=None)
    data["customer"] = pd.read_csv(dir_path + '/customer.csv', header=None)
    data["customer_address"] = pd.read_csv(dir_path + '/customer_address.csv', header=None)
    data["customer_demographics"] = pd.read_csv(dir_path + '/customer_demographics.csv', header=None)
    data["date_dim"] = pd.read_csv(dir_path + '/date_dim.csv', header=None)
    # data["dbgen_version"] = pd.read_csv(dir_path + '/dbgen_version.csv', header=None)
    data["household_demographics"] = pd.read_csv(dir_path + '/household_demographics.csv', header=None)
    data["income_band"] = pd.read_csv(dir_path + '/income_band.csv', header=None)
    data["inventory"] = pd.read_csv(dir_path + '/inventory.csv', header=None)
    data["item"] = pd.read_csv(dir_path + '/item.csv', header=None)
    data["promotion"] = pd.read_csv(dir_path + '/promotion.csv', header=None)
    data["reason"] = pd.read_csv(dir_path + '/reason.csv', header=None)
    data["ship_mode"] = pd.read_csv(dir_path + '/ship_mode.csv', header=None)
    data["store"] = pd.read_csv(dir_path + '/store.csv', header=None)
    data["store_returns"] = pd.read_csv(dir_path + '/store_returns.csv', header=None)
    data["store_sales"] = pd.read_csv(dir_path + '/store_sales.csv', header=None)
    data["time_dim"] = pd.read_csv(dir_path + '/time_dim.csv', header=None)
    data["warehouse"] = pd.read_csv(dir_path + '/warehouse.csv', header=None)
    data["web_page"] = pd.read_csv(dir_path + '/web_page.csv', header=None)
    data["web_returns"] = pd.read_csv(dir_path + '/web_returns.csv', header=None)

    data["web_sales"] = pd.read_csv(dir_path + '/web_sales.csv', header=None)
    data["web_site"] = pd.read_csv(dir_path + '/web_site.csv', header=None)


    call_center_columns = {
        'cc_call_center_sk': 0,
        'cc_call_center_id': 1,
        'cc_rec_start_date': 2,
        'cc_rec_end_date': 3,
        'cc_closed_date_sk': 4,
        'cc_open_date_sk': 5,
        'cc_name': 6,
        'cc_class': 7,
        'cc_employees': 8,
        'cc_sq_ft': 9,
        'cc_hours': 10,
        'cc_manager': 11,
        'cc_mkt_id': 12,
        'cc_mkt_class': 13,
        'cc_mkt_desc': 14,
        'cc_market_manager': 15,
        'cc_division': 16,
        'cc_division_name': 17,
        'cc_company': 18,
        'cc_company_name': 19,
        'cc_street_number': 20,
        'cc_street_name': 21,
        'cc_street_type': 22,
        'cc_suite_number': 23,
        'cc_city': 24,
        'cc_county': 25,
        'cc_state': 26,
        'cc_zip': 27,
        'cc_country': 28,
        'cc_gmt_offset': 29,
        'cc_tax_percentage': 30,
    }

    catalog_page_columns = {
        'cp_catalog_page_sk': 0,
        'cp_catalog_page_id': 1,
        'cp_start_date_sk': 2,
        'cp_end_date_sk': 3,
        'cp_department': 4,
        'cp_catalog_number': 5,
        'cp_catalog_page_number': 6,
        'cp_description': 7,
        'cp_type': 8,
    }

    catalog_returns_columns = {
        'cr_returned_date_sk': 0,
        'cr_returned_time_sk': 1,
        'cr_item_sk': 2,
        'cr_refunded_customer_sk': 3,
        'cr_refunded_cdemo_sk': 4,
        'cr_refunded_hdemo_sk': 5,
        'cr_refunded_addr_sk': 6,
        'cr_returning_customer_sk': 7,
        'cr_returning_cdemo_sk': 8,
        'cr_returning_hdemo_sk': 9,
        'cr_returning_addr_sk': 10,
        'cr_call_center_sk': 11,
        'cr_catalog_page_sk': 12,
        'cr_ship_mode_sk': 13,
        'cr_warehouse_sk': 14,
        'cr_reason_sk': 15,
        'cr_order_number': 16,
        'cr_return_quantity': 17,
        'cr_return_amount': 18,
        'cr_return_tax': 19,
        'cr_return_amt_inc_tax': 20,
        'cr_fee': 21,
        'cr_return_ship_cost': 22,
        'cr_refunded_cash': 23,
        'cr_reversed_charge': 24,
        'cr_store_credit': 25,
        'cr_net_loss': 26,

    }

    catalog_sales_columns = {
        'cs_sold_date_sk': 0,
        'cs_sold_time_sk': 1,
        'cs_ship_date_sk': 2,
        'cs_bill_customer_sk': 3,
        'cs_bill_cdemo_sk': 4,
        'cs_bill_hdemo_sk': 5,
        'cs_bill_addr_sk': 6,
        'cs_ship_customer_sk': 7,
        'cs_ship_cdemo_sk': 8,
        'cs_ship_hdemo_sk': 9,
        'cs_ship_addr_sk': 10,
        'cs_call_center_sk': 11,
        'cs_catalog_page_sk': 12,
        'cs_ship_mode_sk': 13,
        'cs_warehouse_sk': 14,
        'cs_item_sk': 15,
        'cs_promo_sk': 16,
        'cs_order_number': 17,
        'cs_quantity': 18,
        'cs_wholesale_cost': 19,
        'cs_list_price': 20,
        'cs_sales_price': 21,
        'cs_ext_discount_amt': 22,
        'cs_ext_sales_price': 23,
        'cs_ext_wholesale_cost': 24,
        'cs_ext_list_price': 25,
        'cs_ext_tax': 26,
        'cs_coupon_amt': 27,
        'cs_ext_ship_cost': 28,
        'cs_net_paid': 29,
        'cs_net_paid_inc_tax': 30,
        'cs_net_paid_inc_ship': 31,
        'cs_net_paid_inc_ship_tax': 32,
        'cs_net_profit': 33,

    }

    customer_columns = {
        'c_customer_sk': 0,
        'c_customer_id': 1,
        'c_current_cdemo_sk': 2,
        'c_current_hdemo_sk': 3,
        'c_current_addr_sk': 4,
        'c_first_shipto_date_sk': 5,
        'c_first_sales_date_sk': 6,
        'c_salutation': 7,
        'c_first_name': 8,
        'c_last_name': 9,
        'c_preferred_cust_flag': 10,
        'c_birth_day': 11,
        'c_birth_month': 12,
        'c_birth_year': 13,
        'c_birth_country': 14,
        'c_login': 15,
        'c_email_address': 16,
        'c_last_review_date_sk': 17,
    }

    customer_address_columns = {
        'ca_address_sk': 0,
        'ca_address_id': 1,
        'ca_street_number': 2,
        'ca_street_name': 3,
        'ca_street_type': 4,
        'ca_suite_number': 5,
        'ca_city': 6,
        'ca_county': 7,
        'ca_state': 8,
        'ca_zip': 9,
        'ca_country': 10,
        'ca_gmt_offset': 11,
        'ca_location_type': 12,
    }

    customer_demographics_columns = {
        'cd_demo_sk': 0,
        'cd_gender': 1,
        'cd_marital_status': 2,
        'cd_education_status': 3,
        'cd_purchase_estimate': 4,
        'cd_credit_rating': 5,
        'cd_dep_count': 6,
        'cd_dep_employed_count': 7,
        'cd_dep_college_count': 8,

    }

    date_dim_columns = {
        'd_date_sk': 0,
        'd_date_id': 1,
        'd_date': 2,
        'd_month_seq': 3,
        'd_week_seq': 4,
        'd_quarter_seq': 5,
        'd_year': 6,
        'd_dow': 7,
        'd_moy': 8,
        'd_dom': 9,
        'd_qoy': 10,
        'd_fy_year': 11,
        'd_fy_quarter_seq': 12,
        'd_fy_week_seq': 13,
        'd_day_name': 14,
        'd_quarter_name': 15,
        'd_holiday': 16,
        'd_weekend': 17,
        'd_following_holiday': 18,
        'd_first_dom': 19,
        'd_last_dom': 20,
        'd_same_day_ly': 21,
        'd_same_day_lq': 22,
        'd_current_day': 23,
        'd_current_week': 24,
        'd_current_month': 25,
        'd_current_quarter': 26,
        'd_current_year': 27,

    }

    household_demographics_columns = {
        'hd_demo_sk': 0,
        'hd_income_band_sk': 1,
        'hd_buy_potential': 2,
        'hd_dep_count': 3,
        'hd_vehicle_count': 4,

    }

    income_band_columns = {
        'ib_income_band_sk': 0,
        'ib_lower_bound': 1,
        'ib_upper_bound': 2,

    }

    inventory_columns = {
        'inv_date_sk': 0,
        'inv_item_sk': 1,
        'inv_warehouse_sk': 2,
        'inv_quantity_on_hand': 3,

    }

    item_columns = {
        'i_item_sk': 0,
        'i_item_id': 1,
        'i_rec_start_date': 2,
        'i_rec_end_date': 3,
        'i_item_desc': 4,
        'i_current_price': 5,
        'i_wholesale_cost': 6,
        'i_brand_id': 7,
        'i_brand': 8,
        'i_class_id': 9,
        'i_class': 10,
        'i_category_id': 11,
        'i_category': 12,
        'i_manufact_id': 13,
        'i_manufact': 14,
        'i_size': 15,
        'i_formulation': 16,
        'i_color': 17,
        'i_units': 18,
        'i_container': 19,
        'i_manager_id': 20,
        'i_product_name': 21,
    }

    promotion_columns = {
        'p_promo_sk': 0,
        'p_promo_id': 1,
        'p_start_date_sk': 2,
        'p_end_date_sk': 3,
        'p_item_sk': 4,
        'p_cost': 5,
        'p_response_target': 6,
        'p_promo_name': 7,
        'p_channel_dmail': 8,
        'p_channel_email': 9,
        'p_channel_catalog': 10,
        'p_channel_tv': 11,
        'p_channel_radio': 12,
        'p_channel_press': 13,
        'p_channel_event': 14,
        'p_channel_demo': 15,
        'p_channel_details': 16,
        'p_purpose': 17,
        'p_discount_active': 18,
    }

    reason_columns = {
        'r_reason_sk': 0,
        'r_reason_id': 1,
        'r_reason_desc': 2,
    }

    ship_mode_columns = {
        'sm_ship_mode_sk': 0,
        'sm_ship_mode_id': 1,
        'sm_type': 2,
        'sm_code': 3,
        'sm_carrier': 4,
        'sm_contract': 5,
    }

    store_columns = {
        's_store_sk': 0,
        's_store_id': 1,
        's_rec_start_date': 2,
        's_rec_end_date': 3,
        's_closed_date_sk': 4,
        's_store_name': 5,
        's_number_employees': 6,
        's_floor_space': 7,
        's_hours': 8,
        's_manager': 9,
        's_market_id': 10,
        's_geography_class': 11,
        's_market_desc': 12,
        's_market_manager': 13,
        's_division_id': 14,
        's_division_name': 15,
        's_company_id': 16,
        's_company_name': 17,
        's_street_number': 18,
        's_street_name': 19,
        's_street_type': 20,
        's_suite_number': 21,
        's_city': 22,
        's_county': 23,
        's_state': 24,
        's_zip': 25,
        's_country': 26,
        's_gmt_offset': 27,
        's_tax_precentage': 28,
    }

    store_returns_columns = {
        'sr_returned_date_sk': 0,
        'sr_return_time_sk': 1,
        'sr_item_sk': 2,
        'sr_customer_sk': 3,
        'sr_cdemo_sk': 4,
        'sr_hdemo_sk': 5,
        'sr_addr_sk': 6,
        'sr_store_sk': 7,
        'sr_reason_sk': 8,
        'sr_ticket_number': 9,
        'sr_return_quantity': 10,
        'sr_return_amt': 11,
        'sr_return_tax': 12,
        'sr_return_amt_inc_tax': 13,
        'sr_fee': 14,
        'sr_return_ship_cost': 15,
        'sr_refunded_cash': 16,
        'sr_reversed_charge': 17,
        'sr_store_credit': 18,
        'sr_net_loss': 19,
    }

    store_sales_columns = {
        'ss_sold_date_sk': 0,
        'ss_sold_time_sk': 1,
        'ss_item_sk': 2,
        'ss_customer_sk': 3,
        'ss_cdemo_sk': 4,
        'ss_hdemo_sk': 5,
        'ss_addr_sk': 6,
        'ss_store_sk': 7,
        'ss_promo_sk': 8,
        'ss_ticket_number': 9,
        'ss_quantity': 10,
        'ss_wholesale_cost': 11,
        'ss_list_price': 12,
        'ss_sales_price': 13,
        'ss_ext_discount_amt': 14,
        'ss_ext_sales_price': 15,
        'ss_ext_wholesale_cost': 16,
        'ss_ext_list_price': 17,
        'ss_ext_tax': 18,
        'ss_coupon_amt': 19,
        'ss_net_paid': 20,
        'ss_net_paid_inc_tax': 21,
        'ss_net_profit': 22,
    }

    time_dim_columns = {
        't_time_sk': 0,
        't_time_id': 1,
        't_time': 2,
        't_hour': 3,
        't_minute': 4,
        't_second': 5,
        't_am_pm': 6,
        't_shift': 7,
        't_sub_shift': 8,
        't_meal_time': 9,

    }

    warehouse_columns = {
        'w_warehouse_sk': 0,
        'w_warehouse_id': 1,
        'w_warehouse_name': 2,
        'w_warehouse_sq_ft': 3,
        'w_street_number': 4,
        'w_street_name': 5,
        'w_street_type': 6,
        'w_suite_number': 7,
        'w_city': 8,
        'w_county': 9,
        'w_state': 10,
        'w_zip': 11,
        'w_country': 12,
        'w_gmt_offset': 13,

    }
    web_page_columns = {
        'wp_web_page_sk': 0,
        'wp_web_page_id': 1,
        'wp_rec_start_date': 2,
        'wp_rec_end_date': 3,
        'wp_creation_date_sk': 4,
        'wp_access_date_sk': 5,
        'wp_autogen_flag': 6,
        'wp_customer_sk': 7,
        'wp_url': 8,
        'wp_type': 9,
        'wp_char_count': 10,
        'wp_link_count': 11,
        'wp_image_count': 12,
        'wp_max_ad_count': 13,

    }

    web_returns_columns = {
        'wr_returned_date_sk': 0,
        'wr_returned_time_sk': 1,
        'wr_item_sk': 2,
        'wr_refunded_customer_sk': 3,
        'wr_refunded_cdemo_sk': 4,
        'wr_refunded_hdemo_sk': 5,
        'wr_refunded_addr_sk': 6,
        'wr_returning_customer_sk': 7,
        'wr_returning_cdemo_sk': 8,
        'wr_returning_hdemo_sk': 9,
        'wr_returning_addr_sk': 10,
        'wr_web_page_sk': 11,
        'wr_reason_sk': 12,
        'wr_order_number': 13,
        'wr_return_quantity': 14,
        'wr_return_amt': 15,
        'wr_return_tax': 16,
        'wr_return_amt_inc_tax': 17,
        'wr_fee': 18,
        'wr_return_ship_cost': 19,
        'wr_refunded_cash': 20,
        'wr_reversed_charge': 21,
        'wr_account_credit': 22,
        'wr_net_loss': 23,

    }
    web_sales_columns = {
        'ws_sold_date_sk': 0,
        'ws_sold_time_sk': 1,
        'ws_ship_date_sk': 2,
        'ws_item_sk': 3,
        'ws_bill_customer_sk': 4,
        'ws_bill_cdemo_sk': 5,
        'ws_bill_hdemo_sk': 6,
        'ws_bill_addr_sk': 7,
        'ws_ship_customer_sk': 8,
        'ws_ship_cdemo_sk': 9,
        'ws_ship_hdemo_sk': 10,
        'ws_ship_addr_sk': 11,
        'ws_web_page_sk': 12,
        'ws_web_site_sk': 13,
        'ws_ship_mode_sk': 14,
        'ws_warehouse_sk': 15,
        'ws_promo_sk': 16,
        'ws_order_number': 17,
        'ws_quantity': 18,
        'ws_wholesale_cost': 19,
        'ws_list_price': 20,
        'ws_sales_price': 21,
        'ws_ext_discount_amt': 22,
        'ws_ext_sales_price': 23,
        'ws_ext_wholesale_cost': 24,
        'ws_ext_list_price': 25,
        'ws_ext_tax': 26,
        'ws_coupon_amt': 27,
        'ws_ext_ship_cost': 28,
        'ws_net_paid': 29,
        'ws_net_paid_inc_tax': 30,
        'ws_net_paid_inc_ship': 31,
        'ws_net_paid_inc_ship_tax': 32,
        'ws_net_profit': 33,

    }
    web_site_columns = {
        'web_site_sk': 0,
        'web_site_id': 1,
        'web_rec_start_date': 2,
        'web_rec_end_date': 3,
        'web_name': 4,
        'web_open_date_sk': 5,
        'web_close_date_sk': 6,
        'web_class': 7,
        'web_manager': 8,
        'web_mkt_id': 9,
        'web_mkt_class': 10,
        'web_mkt_desc': 11,
        'web_market_manager': 12,
        'web_company_id': 13,
        'web_company_name': 14,
        'web_street_number': 15,
        'web_street_name': 16,
        'web_street_type': 17,
        'web_suite_number': 18,
        'web_city': 19,
        'web_county': 20,
        'web_state': 21,
        'web_zip': 22,
        'web_country': 23,
        'web_gmt_offset': 24,
        'web_tax_percentage': 25,
    }

    data["call_center"].columns = call_center_columns
    # print(data)
    data["catalog_page"].columns = catalog_page_columns
    data["catalog_returns"].columns = catalog_returns_columns
    data["catalog_sales"].columns = catalog_sales_columns
    data["customer"].columns = customer_columns
    data["customer_address"].columns = customer_address_columns
    data["customer_demographics"].columns = customer_demographics_columns
    data["date_dim"].columns = date_dim_columns
    # data["dbgen_version"].columns = dbgen_version_columns
    data["household_demographics"].columns = household_demographics_columns
    data["income_band"].columns = income_band_columns
    data["inventory"].columns = inventory_columns
    data["item"].columns = item_columns
    data["promotion"].columns = promotion_columns
    data["reason"].columns = reason_columns
    data["ship_mode"].columns = ship_mode_columns
    data["store"].columns = store_columns
    data["store_returns"].columns = store_returns_columns
    data["store_sales"].columns = store_sales_columns
    data["time_dim"].columns = time_dim_columns
    data["warehouse"].columns = warehouse_columns
    data["web_page"].columns = web_page_columns
    data["web_returns"].columns = web_returns_columns
    data["web_sales"].columns = web_sales_columns
    data["web_site"].columns = web_site_columns

    # data["info_type"].columns = info_type_column
    # data["keyword"].columns = keyword_column
    # data["kind_type"].columns = kind_type_column
    # data["link_type"].columns = link_type_column
    # data["movie_companies"].columns = movie_companies_column
    # data["movie_info"].columns = movie_info_column
    # data["movie_info_idx"].columns = movie_info_idx_column
    # data["movie_keyword"].columns = movie_keyword_column
    # data["movie_link"].columns = movie_link_column
    # data["name"].columns = name_column
    # data["person_info"].columns = person_info_column
    # data["role_type"].columns = role_type_column
    # data["title"].columns = title_column
    return data
