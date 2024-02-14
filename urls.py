from django.urls import path
from companyapp import views

urlpatterns = [
    path('homepage',views.homepage,name='homepage'),
   
    path('adminhomepage',views.adminhomepage,name='adminhomepage'),
    path('thomepage',views.thomepage,name='thomepage'),

    path('taskpage',views.taskpage,name='taskpage'),
    path('addtaskpage',views.addtaskpage,name='addtaskpage'),
    path('addtask',views.addtask,name='addtask'),
    path('pretaskpage',views.pretaskpage,name='pretaskpage'),
    path('submittask/<int:did>',views.submittask,name='submittask'),
    path('uploadtask/<int:did>',views.uploadtask,name='uploadtask'),
    path('teviewtask',views.teviewtask,name='teviewtask'),
    path('submittaskok/<int:did>',views.submittaskok,name='submittaskok'),
    path('viewtask/<int:did>',views.viewtask,name='viewtask'),

    path('topicpage',views.topicpage,name='topicpage'),
    path('addtopicpage',views.addtopicpage,name='addtopicpage'),
    path('addtopic',views.addtopic,name='addtopic'),
    path('pretopicpage',views.pretopicpage,name='pretopicpage'),
    path('teviewtopic',views.teviewtopic,name='teviewtopic'),

    path('maintrfbpage',views.maintrfbpage,name='maintrfbpage'),
    path('trainerfbpage',views.trainerfbpage,name='trainerfbpage'),
    path('addtrainerfb',views.addtrainerfb,name='addtrainerfb'),
    path('trviewfb',views.trviewfb,name='trviewfb'),

    path('afbview',views.afbview,name='afbview'),
    path('atrfbview',views.atrfbview,name='atrfbview'),
    path('atefbview',views.atefbview,name='atefbview'),

    path('traineefbpage',views.traineefbpage,name='traineefbpage'),
    path('addtraineefb',views.addtraineefb,name='addtraineefb'),

    path('',views.log,name='log'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('waitpage',views.waitpage,name='waitpage'),
    path('approve/<int:uid>',views.approve,name='approve'),
    path('regreject/<int:did>',views.regreject,name='regreject'),

    path('setcoursepage',views.setcoursepage,name='setcoursepage'),
     path('copage',views.copage,name='copage'),
    path('settraining<int:cid>',views.settraining,name='settraining'),
    path('addtrainingsection',views.addtrainingsection,name='addtrainingsection'),

    path('registration',views.registration,name='registration'),
    path('regpage',views.regpage,name='regpage'),
    path('trainerreg',views.trainerreg,name='trainerreg'),
    path('tregistration',views.tregistration,name='tregistration'),
    path('trnoti',views.trnoti,name='trnoti'),
    path('ok<int:uid>',views.ok,name='ok'),
    path('tenoti',views.tenoti,name='tenoti'),
    path('teok<int:uid>',views.teok,name='teok'),
    path('teleaveok<int:did>',views.teleaveok,name='teleaveok'),

    path('coursepage',views.coursepage,name='coursepage'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('anoti',views.anoti,name='anoti'),
    path('viewfeedbackpage',views.viewfeedbackpage,name='viewfeedbackpage'),

    path('teissuepage',views.teissuepage,name='teissuepage'),
    path('addteissue',views.addteissue,name='addteissue'),
    path('trissuepage',views.trissuepage,name='trissuepage'),
    path('addtrissue',views.addtrissue,name='addtrissue'),
    path('aviewissue',views.aviewissue,name='aviewissue'),
    path('aviewtrissue',views.aviewtrissue,name='aviewtrissue'),
    path('aviewteissue',views.aviewteissue,name='aviewteissue'),

    path('replytrissue<int:did>',views.replytrissue,name='replytrissue'),
    path('sendreplytr<int:did>',views.sendreplytr,name='sendreplytr'),
    path('replyteissue<int:did>',views.replyteissue,name='replyteissue'),
    path('sendreplyte<int:did>',views.sendreplyte,name='sendreplyte'),

    path('trattendancepage',views.trattendancepage,name='trattendancepage'),
    path('trgiveattendance',views.trgiveattendance,name='trgiveattendance'),
    path('addteattendance',views.addteattendance,name='addteattendance'),
    path('viewteattendance',views.viewteattendance,name='viewteattendance'),

    path('aviewattendance',views.aviewattendance,name='aviewattendance'),
    path('agivetrattendance',views.agivetrattendance,name='agivetrattendance'),
    path('addtrattendance',views.addtrattendance,name='addtrattendance'),
    path('viewtrattendance',views.viewtrattendance,name='viewtrattendance'),
    path('aviewteattendance',views.aviewteattendance,name='aviewteattendance'),
    path('teviewattendance',views.teviewattendance,name='teviewattendance'),
    path('trownattendance',views.trownattendance,name='trownattendance'),

    path('trleave',views.trleave,name='trleave'),
    path('addtrleave',views.addtrleave,name='addtrleave'),
    path('teleave',views.teleave,name='teleave'),
    path('addteleave',views.addteleave,name='addteleave'),
    path('aviewleave',views.aviewleave,name='aviewleave'),
    path('aviewtrleave',views.aviewtrleave,name='aviewtrleave'),
    path('aviewteleave',views.aviewteleave,name='aviewteleave'),
    path('trleaveaccept<int:did>',views.trleaveaccept,name='trleaveaccept'),
    path('trleavereject<int:did>',views.trleavereject,name='trleavereject'),
    path('teleaveaccept<int:did>',views.teleaveaccept,name='teleaveaccept'),
    path('teleavereject<int:did>',views.teleavereject,name='teleavereject'),

    path('aedittrainerpage<int:did>',views.aedittrainerpage,name='aedittrainerpage'),
    path('aedittrainer<int:did>',views.aedittrainer,name='aedittrainer'),
    path('removetrainer<int:did>',views.removetrainer,name='removetrainer'),
    path('removetrainee<int:did>',views.removetrainee,name='removetrainee'),

    path('triok<int:did>',views.triok,name='triok'),
    path('topicok<int:did>',views.topicok,name='topicok'),
    path('teiok<int:did>',views.teiok,name='teiok'),

    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('setforgotpass',views.setforgotpass,name='setforgotpass'),

    path('trcard<int:did>',views.trcard,name='trcard'),
    path('tecard<int:did>',views.tecard,name='tecard'),
    path('aviewtask<int:did>',views.aviewtask,name='aviewtask'),
    path('workpage<int:did>',views.workpage,name='workpage'),

    path('logout',views.logout,name='logout'),
   
]