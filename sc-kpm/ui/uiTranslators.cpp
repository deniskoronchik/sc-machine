/*
-----------------------------------------------------------------------------
This source file is part of OSTIS (Open Semantic Technology for Intelligent Systems)
For the latest info, see http://www.ostis.net

Copyright (c) 2012 OSTIS

OSTIS is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OSTIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with OSTIS.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------------
*/

#include "uiPrecompiled.h"
#include "uiTranslators.h"
#include "uiKeynodes.h"

#include "translators/uiSc2ScsTranslator.h"

sc_event *ui_translator_sc2scs_event = (sc_event*)nullptr;

void ui_initialize_translators()
{
    ui_translator_sc2scs_event = sc_event_new(ui_keynode_ui_command_translate_from_sc, SC_EVENT_ADD_OUTPUT_ARC, 0, Sc2ScsTranslator::ui_translate_sc2scs, 0);
}

void ui_shutdown_translators()
{

}

sc_result ui_translate_command_resolve_arguments(sc_addr cmd_addr, sc_addr *output_fmt_addr, sc_addr *source_addr)
{
    sc_iterator5 *it = (sc_iterator5*)nullptr;
    sc_bool fmt_founded = SC_FALSE;
    sc_bool source_founded = SC_FALSE;

    // resolve output format
    it = sc_iterator5_f_a_a_a_f_new(cmd_addr,
                                    sc_type_arc_pos_const_perm,
                                    sc_type_node | sc_type_const,
                                    sc_type_arc_pos_const_perm,
                                    ui_keynode_ui_rrel_output_format);

    while (sc_iterator5_next(it) == SC_TRUE)
    {
        *output_fmt_addr = sc_iterator5_value(it, 2);
        fmt_founded = SC_TRUE;
    }

    sc_iterator5_free(it);

    if (fmt_founded == SC_FALSE)
        return SC_RESULT_ERROR;

    // resolve input construction
    it = sc_iterator5_f_a_a_a_f_new(cmd_addr,
                                    sc_type_arc_pos_const_perm,
                                    sc_type_node | sc_type_const,
                                    sc_type_arc_pos_const_perm,
                                    ui_keynode_ui_rrel_source_sc_construction);

    while (sc_iterator5_next(it) == SC_TRUE)
    {
        *source_addr = sc_iterator5_value(it, 2);
        source_founded = SC_TRUE;
    }

    sc_iterator5_free(it);

    if (source_founded == SC_FALSE)
        return SC_RESULT_ERROR;

    return SC_RESULT_OK;
}

sc_bool ui_translate_resolve_system_identifier(sc_addr el, String &sys_idtf)
{
    sc_addr sys_idtf_addr;
    sc_stream *idtf_stream = 0;
    sc_uint32 idtf_length = 0;
    sc_uint32 read_bytes = 0;
    sc_bool result = SC_FALSE;
    sc_char buffer[32];

    sys_idtf = "";
    if (sc_helper_get_system_identifier(el, &sys_idtf_addr) == SC_RESULT_OK)
    {
        if (sc_memory_get_link_content(sys_idtf_addr, &idtf_stream) == SC_RESULT_OK)
        {
            sc_stream_get_length(idtf_stream, &idtf_length);
            while (sc_stream_eof(idtf_stream) == SC_FALSE)
            {
                sc_stream_read_data(idtf_stream, buffer, idtf_length, &read_bytes);
                sys_idtf.append(buffer, read_bytes);
            }
            sc_stream_free(idtf_stream);

            result = SC_TRUE;
        }
    }

    if (result == SC_FALSE)
    {
        StringStream ss;

        ss << el.seg << "_" << el.offset;
        sys_idtf = ss.str();
        return SC_FALSE;
    }

    return result;
}
