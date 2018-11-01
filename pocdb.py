#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 漏洞字典
referer: unknow
author: Lucifer
description: 引入main接口
'''
from cms.cmsmain import *
from system.systemmain import *
from industrial.industrialmain import *
from hardware.hardwaremain import *
from information.informationmain import *
class pocdb_pocs:
    def __init__(self, url):
        self.url = url
        self.informationpocdict = {
            "spring boot 路径泄露":springboot_api_BaseVerify(url),
            "options方法开启":options_method_BaseVerify(url),
            "git源码泄露扫描":git_check_BaseVerify(url),
            "java配置文件文件发现":jsp_conf_find_BaseVerify(url),
            "robots文件发现":robots_find_BaseVerify(url),
            "svn源码泄露扫描":svn_check_BaseVerify(url),
            "JetBrains IDE workspace.xml文件泄露":jetbrains_ide_workspace_disclosure_BaseVerify(url),
            "apache server-status信息泄露":apache_server_status_disclosure_BaseVerify(url),
            "crossdomain.xml文件发现":crossdomain_find_BaseVerify(url),
        }
        self.cmspocdict = {
            "泛微OA downfile.php 任意文件下载漏洞":weaver_oa_filedownload_BaseVerify(url),
            "泛微OA filedownaction SQL注入":weaver_oa_download_sqli_BaseVerify(url),
            "泛微OA 数据库配置泄露":weaver_oa_db_disclosure_BaseVerify(url),
            "phpok res_action_control.php 任意文件下载(需要cookies文件)":phpok_res_action_control_filedownload_BaseVerify(url),
            "phpok api.php SQL注入漏洞":phpok_api_param_sqli_BaseVerify(url),
            "phpok remote_image getshell漏洞":phpok_remote_image_getshell_BaseVerify(url),
            "jeecg 重置admin密码":jeecg_pwd_reset_BaseVerify(url),
            "typecho install.php反序列化命令执行":typecho_install_code_exec_BaseVerify(url),
            "Dotnetcms(风讯cms)SQL注入漏洞":foosun_City_ajax_sqli_BaseVerify(url),
            "韩国autoset建站程序phpmyadmin任意登录漏洞":autoset_phpmyadmin_unauth_BaseVerify(url),
            "phpstudy探针":phpstudy_probe_BaseVerify(url),
            "phpstudy phpmyadmin默认密码漏洞":phpstudy_phpmyadmin_defaultpwd_BaseVerify(url),
            "Discuz论坛forum.php参数message SSRF漏洞":discuz_forum_message_ssrf_BaseVerify(url),
            "Discuz X3 focus.swf flashxss漏洞":discuz_focus_flashxss_BaseVerify(url),
            "Discuz! X2.5 物理路径泄露漏洞":discuz_x25_path_disclosure_BaseVerify(url),
            "Discuz问卷调查参数orderby注入漏洞":discuz_plugin_ques_sqli_BaseVerify(url),
            "Hishop系统productlist.aspx SQL注入":hishop_productlist_sqli_BaseVerify(url),
            "亿邮邮箱弱口令列表泄露":eyou_weakpass_BaseVerify(url),
            "亿邮Email Defender系统免登陆DBA注入":eyou_admin_id_sqli_BaseVerify(url),
            "亿邮邮件系统重置密码问题暴力破解":eyou_resetpw_BaseVerify(url),
            "亿邮mail5 user 参数kw SQL注入":eyou_user_kw_sqli_BaseVerify(url),
            "金蝶办公系统任意文件下载":kingdee_filedownload_BaseVerify(url),
            "金蝶协同平台远程信息泄露漏洞":kingdee_resin_dir_path_disclosure_BaseVerify(url),
            "金蝶AES系统Java web配置文件泄露":kingdee_conf_disclosure_BaseVerify(url),
            "金蝶EAS任意文件读取":kingdee_logoImgServlet_fileread_BaseVerify(url),
            "乐语客服系统任意文件下载漏洞":looyu_down_filedownload_BaseVerify(url),
            "smartoa 多处任意文件下载漏洞":smartoa_multi_filedownload_BaseVerify(url),
            "urp查询接口曝露":urp_query_BaseVerify(url),
            "URP越权查看任意学生课表、成绩(需登录)":urp_query2_BaseVerify(url),
            "URP综合教务系统任意文件读取":urp_ReadJavaScriptServlet_fileread_BaseVerify(url),
            "pkpmbs工程质量监督站信息管理系统SQL注入":pkpmbs_guestbook_sqli_BaseVerify(url),
            "pkpmbs建设工程质量监督系统注入":pkpmbs_addresslist_keyword_sqli_BaseVerify(url),
            "pkpmbs建设工程质量监督系统SQL注入":pkpmbs_MsgList_sqli_BaseVerify(url),
            "帝友P2P借贷系统无需登录SQL注入漏洞":dyp2p_latesindex_sqli_BaseVerify(url),
            "帝友P2P借贷系统任意文件读取漏洞":dyp2p_url_fileread_BaseVerify(url),
            "iGenus邮件系统一处无需登录的任意代码执行":igenus_code_exec_BaseVerify(url),
            "iGenus邮箱系统login.php 参数Lang任意文件读取":igenus_login_Lang_fileread_BaseVerify(url),
            "iGenus邮箱系统管理中心sys/login.php 参数Lang任意文件读取":igenus_syslogin_Lang_fileread_BaseVerify(url),
            "live800客服系统downlog任意文件下载":live800_downlog_filedownload_BaseVerify(url),
            "live800在线客服系统loginAction SQL注入漏洞":live800_loginAction_sqli_BaseVerify(url),
            "live800在线客服系统多处SQL注入GETSHELL漏洞":live800_sta_export_sqli_BaseVerify(url),
            "live800在线客服系统XML实体注入漏洞":live800_services_xxe_BaseVerify(url),
            "live800 fileDownloadServer文件读取漏洞":live800_fileDownloadServer_fileread_BaseVerify(url),
            "Onethink 参数category SQL注入":onethink_category_sqli_BaseVerify(url),
            "ThinkPHP 代码执行漏洞":thinkphp_code_exec_BaseVerify(url),
            "汇思学习管理系统任意文件下载":wizbank_download_filedownload_BaseVerify(url),
            "Cyberwisdom wizBank学习管理平台SQL注入漏洞":wizbank_usr_id_sqli_BaseVerify(url),
            "domino_unauth未授权漏洞":domino_unauth_BaseVerify(url),
            "宏景EHR系统多处SQL注入":hjsoft_sqli_BaseVerify(url),
            "汇能群管理系统SQL注入":hnkj_researchinfo_dan_sqli_BaseVerify(url),
            "汇文软件图书管理系统ajax_asyn_link.old.php任意文件读取":libsys_ajax_asyn_link_old_fileread_BaseVerify(url),
            "汇文软件图书管理系统ajax_asyn_link.php任意文件读取":libsys_ajax_asyn_link_fileread_BaseVerify(url),
            "汇文软件图书管理系统ajax_get_file.php任意文件读取":libsys_ajax_get_file_fileread_BaseVerify(url),
            "通元建站系统用户名泄露漏洞":gpower_users_disclosure_BaseVerify(url),
            "metinfo5.0 getpassword.php两处时间盲注漏洞":metinfo_getpassword_sqli_BaseVerify(url),
            "用友ICC struts2远程命令执行":yonyou_icc_struts2_BaseVerify(url),
            "V2视频会议系统某处SQL注射、XXE漏洞(可getshell)":v2Conference_sqli_xxe_BaseVerify(url),
            "政府采购系统eweb编辑器默认口令Getshell漏洞":gpcsoft_ewebeditor_weak_BaseVerify(url),
            "RAP接口平台struts远程代码执行":rap_interface_struts_exec_BaseVerify(url),
            "虹安DLP数据泄露防护平台struts2远程命令执行":hongan_dlp_struts_exec_BaseVerify(url),
            "九羽数字图书馆struts远程命令执行":jiuyu_library_struts_exec_BaseVerify(url),
            "垚捷电商平台通用struts命令执行":yaojie_steel_struts_exec_BaseVerify(url),
            "Digital-Campus数字校园平台LOG文件泄露":digital_campus_log_disclosure_BaseVerify(url),
            "Digital-Campus2.0数字校园平台Sql注射":digital_campus_systemcodelist_sqli_BaseVerify(url),
            "jeecms download.jsp 参数fpath任意文件下载":jeecms_fpath_filedownload_BaseVerify(url),
            "shopex敏感信息泄露":shopex_phpinfo_disclosure_BaseVerify(url),
            "动科(dkcms)默认数据库漏洞":dkcms_database_disclosure_BaseVerify(url),
            "FineCMS免费版文件上传漏洞":finecms_uploadfile_BaseVerify(url),
            "DaMall商城系统sql注入":damall_selloffer_sqli_BaseVerify(url),
            "大汉版通JCMS数据库配置文件读取漏洞":hanweb_readxml_fileread_BaseVerify(url),
            "大汉downfile.jsp 任意文件下载":hanweb_downfile_filedownload_BaseVerify(url),
            "大汉VerfiyCodeServlet越权漏洞":hanweb_VerifyCodeServlet_install_BaseVerify(url),
            "PHP168 login.php GETSHELL漏洞":php168_login_getshell_BaseVerify(url),
            "dedecms版本探测":dedecms_version_BaseVerify(url),
            "dedecms search.php SQL注入漏洞":dedecms_search_typeArr_sqli_BaseVerify(url),
            "dedecms trace爆路径漏洞":dedecms_error_trace_disclosure_BaseVerify(url),
            "dedecms download.php重定向漏洞":dedecms_download_redirect_BaseVerify(url),
            "dedecms recommend.php SQL注入":dedecms_recommend_sqli_BaseVerify(url),
            "umail物理路径泄露":umail_physical_path_BaseVerify(url),
            "U-Mail邮件系统sessionid访问":umail_sessionid_access_BaseVerify(url),
            "metinfo v5.3sql注入漏洞":metinfo_login_check_sqli_BaseVerify(url),
            "用友致远A6协同系统SQL注射union可shell":yonyou_user_ids_sqli_BaseVerify(url),
            "用友致远A6协同系统多处SQL注入":yonyou_multi_union_sqli_BaseVerify(url),
            "用友致远A6协同系统敏感信息泄露&SQL注射":yonyou_initData_disclosure_BaseVerify(url),
            "用友致远A6协同系统数据库账号泄露":yonyou_createMysql_disclosure_BaseVerify(url),
            "用友致远A6 test.jsp SQL注入":yonyou_test_sqli_BaseVerify(url),
            "用友CRM系统任意文件读取":yonyou_getemaildata_fileread_BaseVerify(url),
            "用友EHR 任意文件读取":yonyou_ehr_ELTextFile_BaseVerify(url),
            "用友优普a8 CmxUserSQL时间盲注入":yonyou_a8_CmxUser_sqli_BaseVerify(url),
            "用友a8 log泄露":yonyou_a8_logs_disclosure_BaseVerify(url),
            "用友a8监控后台默认密码漏洞":yonyou_status_default_pwd_BaseVerify(url),
            "用友致远A8协同系统 blind XML实体注入":yonyou_a8_personService_xxe_BaseVerify(url),
            "用友GRP-U8 sql注入漏洞":yonyou_cm_info_content_sqli_BaseVerify(url),
            "用友u8 CmxItem.php SQL注入":yonyou_u8_CmxItem_sqli_BaseVerify(url),
            "用友FE协作办公平台5.5 SQL注入":yonyou_fe_treeXml_sqli_BaseVerify(url),
            "用友EHR系统 ResetPwd.jsp SQL注入":yonyou_ehr_resetpwd_sqli_BaseVerify(url),
            "用友nc NCFindWeb 任意文件下载漏洞":yonyou_nc_NCFindWeb_fileread_BaseVerify(url),
            "fsmcms p_replydetail.jsp注入漏洞":fsmcms_p_replydetail_sqli_BaseVerify(url),
            "FSMCMS网站重装漏洞":fsmcms_setup_reinstall_BaseVerify(url),
            "FSMCMS columninfo.jsp文件参数ColumnID SQL注入":fsmcms_columninfo_sqli_BaseVerify(url),
            "qibocms知道系统SQL注入":qibocms_search_sqli_BaseVerify(url),
            "qibo分类系统search.php 代码执行":qibocms_search_code_exec_BaseVerify(url),
            "qibocms news/js.php文件参数f_idSQL注入":qibocms_js_f_id_sqli_BaseVerify(url),
            "qibocms s.php文件参数fids SQL注入":qibocms_s_fids_sqli_BaseVerify(url),
            "依友POS系统登陆信息泄露":yeu_disclosure_uid_BaseVerify(url),
            "浪潮行政审批系统十八处注入":inspur_multi_sqli_BaseVerify(url),
            "浪潮ECGAP政务审批系统SQL注入漏洞":inspur_ecgap_displayNewsPic_sqli_BaseVerify(url),
            "五车图书管系统任意下载":clib_kinweblistaction_download_BaseVerify(url),
            "五车图书管系统kindaction任意文件遍历":clib_kindaction_fileread_BaseVerify(url),
            "Gobetters视频会议系统SQL注入漏洞":gobetters_multi_sqli_BaseVerify(url),
            "LBCMS多处SQL注入漏洞":lbcms_webwsfw_bssh_sqli_BaseVerify(url),
            "Euse TMS存在多处DBA权限SQL注入":euse_study_multi_sqli_BaseVerify(url),
            "suntown未授权任意文件上传漏洞":suntown_upfile_fileupload_BaseVerify(url),
            "Dswjcms p2p网贷系统前台4处sql注入":dswjcms_p2p_multi_sqli_BaseVerify(url),
            "skytech政务系统越权漏洞":skytech_bypass_priv_BaseVerify(url),
            "wordpress AzonPop插件SQL注入":wordpress_plugin_azonpop_sqli_BaseVerify(url),
            "wordpress 插件shortcode0.2.3 本地文件包含":wordpress_plugin_ShortCode_lfi_BaseVerify(url),
            "wordpress插件跳转":wordpress_url_redirect_BaseVerify(url),
            "wordpress 插件WooCommerce PHP代码注入":wordpress_woocommerce_code_exec_BaseVerify(url),
            "wordpress 插件mailpress远程代码执行":wordpress_plugin_mailpress_rce_BaseVerify(url),
            "wordpress admin-ajax.php任意文件下载":wordpress_admin_ajax_filedownload_BaseVerify(url),
            "wordpress rest api权限失效导致内容注入":wordpress_restapi_sqli_BaseVerify(url),
            "wordpress display-widgets插件后门漏洞":wordpress_display_widgets_backdoor_BaseVerify(url),
            "Mallbuilder商城系统SQL注入":mallbuilder_change_status_sqli_BaseVerify(url),
            "efuture商业链系统任意文件下载":efuture_downloadAct_filedownload_BaseVerify(url),
            "kj65n煤矿远程监控系统SQL注入":kj65n_monitor_sqli_BaseVerify(url),
            "票友机票预订系统6处SQL注入":piaoyou_multi_sqli_BaseVerify(url),
            "票友机票预订系统10处SQL注入":piaoyou_ten_sqli_BaseVerify(url),
            "票友机票预订系统6处SQL注入(绕过)":piaoyou_six_sqli_BaseVerify(url),
            "票友机票预订系统6处SQL注入2(绕过)":piaoyou_six2_sqli_BaseVerify(url),
            "票友票务系统int_order.aspx SQL注入":piaoyou_int_order_sqli_BaseVerify(url),
            "票友票务系统通用sql注入":piaoyou_newsview_list_BaseVerify(url),
            "中农信达监察平台任意文件下载":sinda_downloadfile_download_BaseVerify(url),
            "连邦行政审批系统越权漏洞":lianbang_multi_bypass_priv_BaseVerify(url),
            "北斗星政务PostSuggestion.aspx SQL注入":star_PostSuggestion_sqli_BaseVerify(url),
            "TCExam重新安装可getshell漏洞":tcexam_reinstall_getshell_BaseVerify(url),
            "合众商道php系统通用注入":hezhong_list_id_sqli_BaseVerify(url),
            "最土团购SQL注入":zuitu_coupon_id_sqli_BaseVerify(url),
            "时光动态网站平台(Cicro 3e WS) 任意文件下载":cicro_DownLoad_filedownload_BaseVerify(url),
            "华飞科技cms绕过JS GETSHELL":huaficms_bypass_js_BaseVerify(url),
            "IWMS系统后台绕过&整站删除":iwms_bypass_js_delete_BaseVerify(url),
            "农友政务系统多处SQL注入":nongyou_multi_sqli_BaseVerify(url),
            "农友政务系统Item2.aspx SQL注入":nongyou_Item2_sqli_BaseVerify(url),
            "农友政务ShowLand.aspx SQL注入":nongyou_ShowLand_sqli_BaseVerify(url),
            "农友多处时间盲注":nongyou_sleep_sqli_BaseVerify(url),
            "某政府采购系统任意用户密码获取漏洞":zfcgxt_UserSecurityController_getpass_BaseVerify(url),
            "铭万事业通用建站系统SQL注入":mainone_b2b_Default_sqli_BaseVerify(url),
            "铭万B2B SupplyList SQL注入漏洞":mainone_SupplyList_sqli_BaseVerify(url),
            "铭万门户建站系统ProductList SQL注入":mainone_ProductList_sqli_BaseVerify(url),
            "xplus npmaker 2003系统GETSHELL":xplus_2003_getshell_BaseVerify(url),
            "xplus通用注入":xplus_mysql_mssql_sqli_BaseVerify(url),
            "workyi人才系统多处注入漏洞":workyi_multi_sqli_BaseVerify(url),
            "菲斯特诺期刊系统多处SQL注入":newedos_multi_sqli_BaseVerify(url),
            "东软UniPortal1.2未授权访问&SQL注入":uniportal_bypass_priv_sqli_BaseVerify(url),
            "PageAdmin可“伪造”VIEWSTATE执行任意SQL查询&重置管理员密码":pageadmin_forge_viewstate_BaseVerify(url),
            "SiteFactory CMS 5.5.9任意文件下载漏洞":xtcms_download_filedownload_BaseVerify(url),
            "璐华企业版OA系统多处SQL注入":ruvar_oa_multi_sqli_BaseVerify(url),
            "璐华OA系统多处SQL注入":ruvar_oa_multi_sqli2_BaseVerify(url),
            "璐华OA系统多处SQL注入3":ruvar_oa_multi_sqli3_BaseVerify(url),
            "GN SQL Injection":gn_consulting_sqli_BaseVerify(url),
            "JumboECMS V1.6.1 注入漏洞":jumboecms_slide_id_sqli_BaseVerify(url),
            "joomla组件com_docman本地文件包含":joomla_com_docman_lfi_BaseVerify(url),
            "joomla 3.7.0 core SQL注入":joomla_index_list_sqli_BaseVerify(url),
            "北京网达信联电子采购系统多处注入":caitong_multi_sqli_BaseVerify(url),
            "Designed by Alkawebs SQL Injection":alkawebs_viewnews_sqli_BaseVerify(url),
            "一采通电子采购系统多处时间盲注":caitong_multi_sleep_sqli_BaseVerify(url),
            "启博淘店通标准版任意文件遍历漏洞":shop360_do_filedownload_BaseVerify(url),
            "PSTAR-电子服务平台SQL注入漏洞":pstar_warehouse_msg_01_sqli_BaseVerify(url),
            "PSTAR-电子服务平台isfLclInfo注入漏洞":pstar_isfLclInfo_sqli_BaseVerify(url),
            "PSTAR-电子服务平台SQL注入漏洞":pstar_qcustoms_sqli_BaseVerify(url),
            "TRS(拓尔思) wcm pre.as 文件包含":trs_wcm_pre_as_lfi_BaseVerify(url),
            "TRS(拓尔思) 网络信息雷达4.6系统敏感信息泄漏到进后台":trs_inforadar_disclosure_BaseVerify(url),
            "TRS(拓尔思) 学位论文系统papercon处SQL注入":trs_lunwen_papercon_sqli_BaseVerify(url),
            "TRS(拓尔思) infogate插件 blind XML实体注入":trs_infogate_xxe_BaseVerify(url),
            "TRS(拓尔思) infogate插件 任意注册漏洞":trs_infogate_register_BaseVerify(url),
            "TRS(拓尔思) was5配置文件泄露":trs_was5_config_disclosure_BaseVerify(url),
            "TRS(拓尔思) was5 download_templet.jsp任意文件下载":trs_was5_download_templet_BaseVerify(url),
            "TRS(拓尔思) wcm系统默认账户漏洞":trs_wcm_default_user_BaseVerify(url),
            "TRS(拓尔思) wcm 6.x版本infoview信息泄露":trs_wcm_infoview_disclosure_BaseVerify(url),
            "TRS(拓尔思) was40 passwd.htm页面泄露":trs_was40_passwd_disclosure_BaseVerify(url),
            "TRS(拓尔思) was40 tree导航树泄露":trs_was40_tree_disclosure_BaseVerify(url),
            "TRS(拓尔思) ids身份认证信息泄露":trs_ids_auth_disclosure_BaseVerify(url),
            "TRS(拓尔思) wcm webservice文件写入漏洞":trs_wcm_service_writefile_BaseVerify(url),
            "易创思ECScms MoreIndex SQL注入":ecscms_MoreIndex_sqli_BaseVerify(url),
            "金窗教务系统存在多处SQL注射漏洞":gowinsoft_jw_multi_sqli_BaseVerify(url),
            "siteserver3.6.4 background_taskLog.aspx注入":siteserver_background_taskLog_sqli_BaseVerify(url),
            "siteserver3.6.4 background_log.aspx注入":siteserver_background_log_sqli_BaseVerify(url),
            "siteserver3.6.4 user.aspx注入":siteserver_UserNameCollection_sqli_BaseVerify(url),
            "siteserver3.6.4 background_keywordsFilting.aspx注入":siteserver_background_keywordsFilting_sqli_BaseVerify(url),
            "siteserver3.6.4 background_administrator.aspx注入":siteserver_background_administrator_sqli_BaseVerify(url),
            "NITC营销系统suggestwordList.php SQL注入":nitc_suggestwordList_sqli_BaseVerify(url),
            "NITC营销系统index.php SQL注入":nitc_index_language_id_sqli_BaseVerify(url),
            "南大之星信息发布系统DBA SQL注入":ndstar_six_sqli_BaseVerify(url),
            "蓝凌EIS智慧协同平台menu_left_edit.aspx SQL注入":eis_menu_left_edit_sqli_BaseVerify(url),
            "天柏在线培训系统Type_List.aspx SQL注入":tianbo_Type_List_sqli_BaseVerify(url),
            "天柏在线培训系统TCH_list.aspx SQL注入":tianbo_TCH_list_sqli_BaseVerify(url),
            "天柏在线培训系统Class_Info.aspx SQL注入":tianbo_Class_Info_sqli_BaseVerify(url),
            "天柏在线培训系统St_Info.aspx SQL注入":tianbo_St_Info_sqli_BaseVerify(url),
            "安财软件GetXMLList任意文件读取":acsoft_GetXMLList_fileread_BaseVerify(url),
            "安财软件GetFile任意文件读取":acsoft_GetFile_fileread_BaseVerify(url),
            "安财软件GetFileContent任意文件读取":acsoft_GetFileContent_fileread_BaseVerify(url),
            "天津神州助平台通用型任意下载":gxwssb_fileDownloadmodel_download_BaseVerify(url),
            "ETMV9数字化校园平台任意下载":etmdcp_Load_filedownload_BaseVerify(url),
            "安脉grghjl.aspx 参数stuNo注入":anmai_grghjl_stuNo_sqli_BaseVerify(url),
            "农友多处时间盲注":nongyou_ShowLand_sqli_BaseVerify(url),
            "某政府通用任意文件下载":zf_cms_FileDownload_BaseVerify(url),
            "师友list.aspx keywords SQL注入":shiyou_list_keyWords_sqli_BaseVerify(url),
            "speedcms list文件参数cid SQL注入":speedcms_list_cid_sqli_BaseVerify(url),
            "卓繁cms任意文件下载漏洞":zhuofan_downLoadFile_download_BaseVerify(url),
            "金宇恒内容管理系统通用型任意文件下载漏洞":gevercms_downLoadFile_filedownload_BaseVerify(url),
            "任我行crm任意文件下载":weway_PictureView1_filedownload_BaseVerify(url),
            "易创思教育建站系统未授权访问可查看所有注册用户":esccms_selectunitmember_unauth_BaseVerify(url),
            "wecenter SQL注入":wecenter_topic_id_sqli_BaseVerify(url),
            "shopnum1 ShoppingCart1 SQL注入":shopnum_ShoppingCart1_sqli_BaseVerify(url),
            "shopnum1 ProductListCategory SQL注入":shopnum_ProductListCategory_sqli_BaseVerify(url),
            "shopnum1 ProductDetail.aspx SQL注入":shopnum_ProductDetail_sqli_BaseVerify(url),
            "shopnum1 GuidBuyList.aspx SQL注入":shopnum_GuidBuyList_sqli_BaseVerify(url),
            "好视通视频会议系统(fastmeeting)任意文件遍历":fastmeeting_download_filedownload_BaseVerify(url),
            "远古流媒体系统两处SQL注入":viewgood_two_sqli_BaseVerify(url),
            "远古 pic_proxy.aspx SQL注入":viewgood_pic_proxy_sqli_BaseVerify(url),
            "远古流媒体系统  GetCaption.ashx注入":viewgood_GetCaption_sqli_BaseVerify(url),
            "shop7z order_checknoprint.asp SQL注入":shop7z_order_checknoprint_sqli_BaseVerify(url),
            "dreamgallery album.php SQL注入":dreamgallery_album_id_sqli_BaseVerify(url),
            "IPS Community Suite <= 4.1.12.3 PHP远程代码执行":ips_community_suite_code_exec_BaseVerify(url),
            "科信邮件系统login.server.php 时间盲注":kxmail_login_server_sqli_BaseVerify(url),
            "shopNC B2B版 index.php SQL注入":shopnc_index_class_id_sqli_BaseVerify(url),
            "南京擎天政务系统 geren_list_page.aspx SQL注入":skytech_geren_list_page_sqli_BaseVerify(url),
            "学子科技诊断测评系统多处未授权访问":xuezi_ceping_unauth_BaseVerify(url),
            "Shadows-IT selector.php 任意文件包含":shadowsit_selector_lfi_BaseVerify(url),
            "皓翰数字化校园平台任意文件下载":haohan_FileDown_filedownload_BaseVerify(url),
            "phpcms digg_add.php SQL注入":phpcms_digg_add_sqli_BaseVerify(url),
            "phpcms authkey泄露漏洞":phpcms_authkey_disclosure_BaseVerify(url),
            "phpcms2008 flash_upload.php SQL注入":phpcms_flash_upload_sqli_BaseVerify(url),
            "phpcms2008 product.php 代码执行":phpcms_product_code_exec_BaseVerify(url),
            "phpcms v9.6.0 SQL注入":phpcms_v96_sqli_BaseVerify(url),
            "phpcms 9.6.1任意文件读取漏洞":phpcms_v961_fileread_BaseVerify(url),
            "phpcms v9 flash xss漏洞":phpcms_v9_flash_xss_BaseVerify(url),
            "seacms search.php 代码执行":seacms_search_code_exec_BaseVerify(url),
            "seacms 6.45 search.php order参数前台代码执行":seacms_order_code_exec_BaseVerify(url),
            "seacms search.php 参数jq代码执行":seacms_search_jq_code_exec_BaseVerify(url),
            "安脉学生管理系统10处SQL注入":anmai_teachingtechnology_sqli_BaseVerify(url),
            "cmseasy header.php 报错注入":cmseasy_header_detail_sqli_BaseVerify(url),
            "PhpMyAdmin2.8.0.3无需登录任意文件包含导致代码执行":phpmyadmin_setup_lfi_BaseVerify(url),
            "opensns index.php 参数arearank注入":opensns_index_arearank_BaseVerify(url),
            "opensns index.php 前台getshell":opensns_index_getshell_BaseVerify(url),
            "ecshop uc.php参数code SQL注入":ecshop_uc_code_sqli_BaseVerify(url),
            "ecshop3.0 flow.php 参数order_id注入":ecshop_flow_orderid_sqli_BaseVerify(url),
            "SiteEngine 6.0 & 7.1 SQL注入漏洞":siteengine_comments_module_sqli_BaseVerify(url),
            "明腾cms cookie欺骗漏洞":mingteng_cookie_deception_BaseVerify(url),
            "正方教务系统services.asmx SQL注入":zfsoft_service_stryhm_sqli_BaseVerify(url),
            "正方教务系统数据库任意操纵":zfsoft_database_control_BaseVerify(url),
            "正方教务系统default3.aspx爆破页面":zfsoft_default3_bruteforce_BaseVerify(url),
            "1039驾校通未授权访问漏洞":jxt1039_unauth_BaseVerify(url),
            "thinksns category模块代码执行":thinksns_category_code_exec_BaseVerify(url),
            "TPshop eval-stdin.php 代码执行漏洞":tpshop_eval_stdin_code_exec_BaseVerify(url),
        }
        self.industrialpocdict = {
            "新力热电无线抄表监控系统绕过后台登录":wireless_monitor_priv_elevation_BaseVerify(url),
            "火力发电能耗监测弱口令":rockontrol_weak_BaseVerify(url),
            "sgc8000 大型旋转机监控系统报警短信模块泄露":sgc8000_sg8k_sms_disclosure_BaseVerify(url),
            "sgc8000 监控系统数据连接信息泄露":sgc8000_deldata_config_disclosure_BaseVerify(url),
            "sgc8000监控系统超管账号泄露漏洞":sgc8000_defaultuser_disclosure_BaseVerify(url),
            "zte 无线控制器 SQL注入":zte_wireless_getChannelByCountryCode_sqli_BaseVerify(url),
            "中兴无线控制器弱口令":zte_wireless_weak_pass_BaseVerify(url),
            "东方电子SCADA通用系统信息泄露":dfe_scada_conf_disclosure_BaseVerify(url),
        }
        self.systempocdict = {
            "libssh身份绕过漏洞(CVE-2018-10933)":libssh_bypass_auth_BaseVerify(url),
            "ElasticSearch未授权漏洞":elasticsearch_unauth_BaseVerify(url),
            "CouchDB 未授权漏洞":couchdb_unauth_BaseVerify(url),
            "zookeeper 未授权漏洞":zookeeper_unauth_BaseVerify(url),
            "GoAhead LD_PRELOAD远程代码执行(CVE-2017-17562)":goahead_LD_PRELOAD_rce_BaseVerify(url),
            "天融信Topsec change_lan.php本地文件包含":topsec_change_lan_filedownload_BaseVerify(url),
            "Tomcat代码执行漏洞(CVE-2017-12616)":tomcat_put_exec_BaseVerify(url),
            "Tomcat 弱口令漏洞":tomcat_weak_pass_BaseVerify(url),
            "redis 未授权漏洞":redis_unauth_BaseVerify(url),
            "KingGate防火墙默认配置不当可被远控":kinggate_zebra_conf_BaseVerify(url),
            "nginx Multi-FastCGI Code Execution":multi_fastcgi_code_exec_BaseVerify(url),
            "TurboMail设计缺陷以及默认配置漏洞":turbomail_conf_BaseVerify(url),
            "TurboGate邮件网关XXE漏洞":turbogate_services_xxe_BaseVerify(url),
            "weblogic blind XXE漏洞(CVE-2018-3246)":weblogic_ws_utc_xxe_BaseVerify(url),
            "weblogic 弱口令漏洞":weblogic_weak_pass_BaseVerify(url),
            "weblogic SSRF漏洞(CVE-2014-4210)":weblogic_ssrf_BaseVerify(url),
            "weblogic XMLdecoder反序列化漏洞(CVE-2017-10271)":weblogic_xmldecoder_exec_BaseVerify(url),
            "weblogic 接口泄露":weblogic_interface_disclosure_BaseVerify(url),
            "实易DNS管理系统文件包含至远程代码执行":forease_fileinclude_code_exec_BaseVerify(url),
            "hudson源代码泄露漏洞":hudson_ws_disclosure_BaseVerify(url),
            "N点虚拟主机管理系统V1.9.6版数据库下载漏洞":npoint_mdb_download_BaseVerify(url),
            "宏杰Zkeys虚拟主机默认数据库漏洞":zkeys_database_conf_BaseVerify(url),
            "江南科友堡垒机信息泄露":hac_gateway_info_disclosure_BaseVerify(url),
            "Moxa OnCell 未授权访问":moxa_oncell_telnet_BaseVerify(url),
            "glassfish 任意文件读取":glassfish_fileread_BaseVerify(url),
            "zabbix jsrpc.php SQL注入":zabbix_jsrpc_profileIdx2_sqli_BaseVerify(url),
            "php fastcgi任意文件读取漏洞":php_fastcgi_read_BaseVerify(url),
            "php expose_php模块开启":php_expose_disclosure_BaseVerify(url),
            "hfs rejetto 远程代码执行":hfs_rejetto_search_rce_BaseVerify(url),
            "shellshock漏洞":shellshock_BaseVerify(url),
            "dorado默认口令漏洞":dorado_default_passwd_BaseVerify(url),
            "ms15_034 http.sys远程代码执行(CVE-2015-1635)":iis_ms15034_httpsys_rce_BaseVerify(url),
            "IIS 6.0 webdav远程代码执行漏洞(CVE-2017-7269)":iis_webdav_rce_BaseVerify(url),
            "深澜软件srun3000计费系统任意文件下载漏洞":srun_index_file_filedownload_BaseVerify(url),
            "深澜软件srun3000计费系统rad_online.php命令执行bypass":srun_rad_online_bypass_rce_BaseVerify(url),
            "深澜软件srun3000计费系统rad_online.php参数username命令执行":srun_rad_online_username_rce_BaseVerify(url),
            "深澜软件srun3000计费系统download.php任意文件下载":srun_download_file_filedownload_BaseVerify(url),
            "深澜软件srun3000计费系统user_info.php命令执行":srun_user_info_uid_rce_BaseVerify(url),
            "intel AMT web系统绕过登录(CVE-2017-5689)":intel_amt_crypt_bypass_BaseVerify(url),
            "smtp starttls明文命令注入(CVE-2011-0411)":smtp_starttls_plaintext_inj_BaseVerify(url),
            "resin viewfile 任意文件读取":resin_viewfile_fileread_BaseVerify(url),
            "mongodb 未授权漏洞":mongodb_unauth_BaseVerify(url),
            "深信服 AD4.5版本下命令执行漏洞":sangfor_ad_script_command_exec_BaseVerify(url),
        }
        self.hardwarepocdict = {
            "Dlink 本地文件包含":router_dlink_webproc_fileread_BaseVerify(url),
            "Dlink DIAGNOSTIC.PHP命令执行":router_dlink_command_exec_BaseVerify(url),
            "锐捷VPN设备未授权访问漏洞":router_ruijie_unauth_BaseVerify(url),
            "上海安达通某网关产品&某VPN产品struts命令执行":adtsec_gateway_struts_exec_BaseVerify(url),
            "SJW74系列安全网关 和 PN-2G安全网关信息泄露":adtsec_Overall_app_js_bypass_BaseVerify(url),
            "迈普vpn安全网关弱口令&&执行命令":mpsec_weakpass_exec_BaseVerify(url),
            "迈普网关webui任意文件下载":mpsec_webui_filedownload_BaseVerify(url),
            "浙江宇视（DVR/NCR）监控设备远程命令执行漏洞":camera_uniview_dvr_rce_BaseVerify(url),
            "富士施乐打印机默认口令漏洞":printer_xerox_default_pwd_BaseVerify(url),
            "惠普打印机telnet未授权访问":printer_hp_jetdirect_unauth_BaseVerify(url),
            "东芝topaccess打印机未授权漏洞":printer_topaccess_unauth_BaseVerify(url),
            "佳能打印机未授权漏洞":printer_canon_unauth_BaseVerify(url),
            "juniper NetScreen防火墙后门(CVE-2015-7755)":juniper_netscreen_backdoor_BaseVerify(url),
            "海康威视web弱口令":camera_hikvision_web_weak_BaseVerify(url),
        }
