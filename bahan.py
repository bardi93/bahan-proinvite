
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        inv1 = op.param3.replace('\x1e',',')
                        inv2 = inv1.split(',')
                        for _mid in inv2:
                            if _mid not in Bots and _mid not in owner and _mid not in admin:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                    except:
                        pass

        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = random.choice(ABC).getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            if _mid in wait["blacklist"]:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass